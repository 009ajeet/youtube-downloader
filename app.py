import os
import uuid
import shutil
from flask import Flask, request, send_file, render_template, jsonify, after_this_request
import yt_dlp

app = Flask(__name__)
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), 'downloads')
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')
    file_type = data.get('type')
    quality = data.get('quality')

    if not url or not file_type or not quality:
        return jsonify({'error': 'Missing required parameters.'}), 400

    unique_id = str(uuid.uuid4())
    outtmpl = os.path.join(DOWNLOAD_FOLDER, f'{unique_id}.%(ext)s')
    ydl_opts = {
        'outtmpl': outtmpl,
        'quiet': True,
        'noplaylist': True,
        'format': None,
    }

    if file_type == 'mp3':
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': quality.replace('kbps', '')
        }]
    elif file_type == 'mp4':
        ydl_opts['format'] = f'bestvideo[height<={quality.replace("p","")}]'+"+bestaudio/best"
        ydl_opts['merge_output_format'] = 'mp4'
    else:
        return jsonify({'error': 'Invalid type.'}), 400

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            if file_type == 'mp3':
                filename = ydl.prepare_filename(info).rsplit('.', 1)[0] + '.mp3'
            else:
                filename = ydl.prepare_filename(info).rsplit('.', 1)[0] + '.mp4'
    except Exception as e:
        return jsonify({'error': f'Error downloading: {str(e)}'}), 500

    @after_this_request
    def remove_file(response):
        try:
            if os.path.exists(filename):
                os.remove(filename)
        except Exception:
            pass
        return response

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
