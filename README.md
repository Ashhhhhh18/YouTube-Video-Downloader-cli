
# 🎬 YouTube Video Downloader CLI (with Metadata)

A simple command-line Python app to download YouTube videos along with key metadata like title, duration, views, and upload date.

## 📦 Features
- Download high-quality YouTube videos
- Merge best audio + video using FFmpeg
- Extract and display metadata:
  - Title
  - Duration (in minutes)
  - Views
  - Upload date
  - Channel name
- Clean CLI interface

## 🛠️ How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Make sure FFmpeg is installed  
Required for merging audio and video.  
[Download FFmpeg](https://www.gyan.dev/ffmpeg/builds/) → Extract → Add `bin/` to system path.

### 3. Run the App
```bash
python main.py
```

### 4. Paste the YouTube video URL when prompted and enjoy! 📥

---

## 📁 Example Output
```
✅ Download Complete!

🔹 Title       : Python Tutorial
🔹 Duration    : 12.3 mins
🔹 Views       : 1,200,000
🔹 Upload Date : 20250701
🔹 Channel     : Tech Channel
🔹 File Name   : Python Tutorial.mp4
```

---

## 📚 Technologies
- Python
- yt-dlp
- FFmpeg

---

## 👨‍💻 Author
Ashok Ash – [GitHub](https://github.com/Ashhhhhh18)
