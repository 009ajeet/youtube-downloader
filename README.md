# 🎵 YouTube Downloader - Premium Web App

A beautiful, full-stack YouTube video/audio downloader with a premium UI experience.

![YouTube Downloader Screenshot](screenshot.png)

## ✨ Features

- 🎵 **MP3 Audio Downloads** - High quality audio extraction (320kbps, 256kbps, 192kbps, 128kbps)
- 🎬 **MP4 Video Downloads** - Multiple quality options (1080p, 720p, 480p, 360p, 240p)
- 🎨 **Premium UI Design** - Modern glass-morphism design with animations
- 📱 **Responsive Design** - Works perfectly on desktop and mobile
- ⚡ **Lightning Fast** - Optimized download process with progress tracking
- 🛡️ **Safe & Secure** - No data storage, files deleted after download
- 🎯 **Easy to Use** - Just paste URL, select quality, and download

## 🚀 Tech Stack

### Backend
- **Python** with Flask framework
- **yt-dlp** for YouTube video/audio processing
- **FFmpeg** for audio conversion
- **UUID** for unique file naming

### Frontend
- **HTML5** with semantic structure
- **CSS3** with modern features (backdrop-filter, grid, flexbox)
- **Vanilla JavaScript** with ES6+ features
- **Font Awesome** icons
- **Inter Font** from Google Fonts

## 📁 Project Structure

```
song-downloader/
├── app.py                 # Flask backend server
├── templates/
│   └── index.html        # Frontend interface
├── downloads/            # Temporary download folder
├── requirements.txt      # Python dependencies
├── run.bat              # Windows batch file to start app
└── README.md            # This file
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7+
- FFmpeg (for MP3 conversion)
- Git (optional)

### 1. Clone the Repository
```bash
git clone https://github.com/009ajeet/youtube-downloader.git
cd youtube-downloader
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg
**Windows:**
```bash
winget install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

### 4. Run the Application
```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000`

## 💻 Usage

1. **Start the Application**: Run `python app.py` or double-click `run.bat` on Windows
2. **Open Browser**: Navigate to `http://127.0.0.1:5000`
3. **Paste YouTube URL**: Copy and paste any YouTube video URL
4. **Choose Format**: Click either "Download MP3" or "Download MP4"
5. **Select Quality**: Choose your preferred quality from the modal
6. **Download**: The file will automatically download to your device

## 🎨 UI Features

- **Glass Morphism Design**: Modern translucent design with backdrop blur
- **Floating Animations**: Subtle background shape animations
- **Quality Selection Modal**: Beautiful modal with animated quality options
- **Progress Indicators**: Real-time download progress with shimmer effects
- **Smart Alerts**: Success/error messages with auto-hide
- **Keyboard Shortcuts**: 
  - `Enter` to start download
  - `Escape` to close modals
- **Responsive Layout**: Optimized for all screen sizes

## 🔧 Configuration

### Supported Quality Options

**MP3 Audio:**
- 320 kbps (Highest Quality)
- 256 kbps (High Quality) 
- 192 kbps (Good Quality)
- 128 kbps (Standard)

**MP4 Video:**
- 1080p (Full HD)
- 720p (HD Ready)
- 480p (Standard)
- 360p (Mobile)
- 240p (Low Quality)

## 🚨 Important Notes

- **Educational Use Only**: This tool is for educational and personal use
- **Respect Copyright**: Only download content you have rights to
- **No Data Storage**: Files are automatically deleted after download
- **FFmpeg Required**: MP3 downloads require FFmpeg installation

## 🐛 Troubleshooting

### Common Issues:

**"FFmpeg not found" error:**
- Install FFmpeg and ensure it's in your system PATH

**"Invalid YouTube URL" error:**
- Make sure the URL contains `youtube.com` or `youtu.be`
- Check that the video is publicly available

**Download fails:**
- Check your internet connection
- Verify the video is not region-locked
- Try a different quality option

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is intended for educational and personal use only. Users are responsible for complying with YouTube's Terms of Service and applicable copyright laws. The developers are not responsible for any misuse of this software.

## 🙏 Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for YouTube downloading capabilities
- [FFmpeg](https://ffmpeg.org/) for audio/video processing
- [Font Awesome](https://fontawesome.com/) for beautiful icons
- [Google Fonts](https://fonts.google.com/) for the Inter font family

---

Made with ❤️ for educational purposes
