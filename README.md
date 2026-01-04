# 📺 Universal Media Downloader

A lightweight, Python-based GUI application that allows users to download video and audio from thousands of websites (including YouTube, Vimeo, Twitch, and news sites).

Built with **Python**, **Tkinter**, and the powerful **yt-dlp** engine.

## ✨ Features
* **Universal Support:** Works on 1,700+ websites.
* **Simple GUI:** User-friendly interface; no command line needed.
* **Smart Downloading:** Automatically selects the best quality video available.
* **Non-Freezing:** Uses threading to keep the application responsive during large downloads.
* **Format Handling:** Automatically merges video and audio streams (requires FFmpeg).

## 🛠️ Prerequisites
Before running the application, ensure you have the following installed:
1.  **Python 3.x**: [Download here](https://www.python.org/downloads/)
2.  **FFmpeg** (Optional but Recommended): Required for merging audio/video on some sites and for high-quality streams.
    * *Windows:* Download from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/), extract, and place `ffmpeg.exe` in this project folder.
    * *Mac:* `brew install ffmpeg`
    * *Linux:* `sudo apt install ffmpeg`

## 📥 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/media-downloader.git](https://github.com/YOUR_USERNAME/media-downloader.git)
    cd media-downloader
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: If you don't have a requirements file, simply run `pip install yt-dlp`)*

## 🚀 Usage

1.  Run the application:
    ```bash
    python my_downloader.py
    ```
2.  Paste the URL of the video you want to download into the input box.
3.  Click **Download Media**.
4.  Watch the status label for progress. The file will be saved in the same folder as the script.

## ⚠️ Disclaimer
**For Educational Purposes Only.**
This tool is intended to be used for downloading copyright-free content or content for which you have the creator's permission. The developer does not endorse or condone the use of this software for piracy or copyright infringement. Please respect the Terms of Service of the websites you visit.

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License
[MIT](https://choosealicense.com/licenses/mit/)
