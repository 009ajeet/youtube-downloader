@echo off
echo ===============================
echo  GitHub Deployment Commands
echo ===============================
echo.
echo 1. First, create a new repository on GitHub.com
echo 2. Then run these commands one by one:
echo.
echo git remote add origin https://github.com/YOURUSERNAME/youtube-downloader.git
echo git push -u origin main
echo.
echo Replace YOURUSERNAME with your actual GitHub username
echo.
echo ===============================
echo  For Heroku Deployment:
echo ===============================
echo.
echo heroku login
echo heroku create your-app-name
echo git push heroku main
echo heroku buildpacks:add --index 1 https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git
echo heroku open
echo.
pause
