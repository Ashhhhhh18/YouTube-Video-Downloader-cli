from yt_dlp import YoutubeDL
import os

def download_video(url):
    options = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s'
    }

    with YoutubeDL(options) as ydl:
        print("\n📥 Downloading video...")
        info = ydl.extract_info(url, download=True)

        print("\n✅ Download Complete!\n")
        print("📄 Video Info:")
        print(f"🔹 Title       : {info.get('title')}")
        print(f"🔹 Duration    : {round(info.get('duration', 0) / 60, 2)} mins")
        print(f"🔹 Views       : {info.get('view_count')}")
        print(f"🔹 Upload Date : {info.get('upload_date')}")
        print(f"🔹 Channel     : {info.get('uploader')}")
        print(f"🔹 File Name   : {ydl.prepare_filename(info)}")

        # Log file size and duration
        download_path = info['requested_downloads'][0]['_filename']
        file_size = os.path.getsize(download_path)
        duration = info.get('duration', 'Unknown')

        print(f"\n📦 File Size   : {file_size / (1024 * 1024):.2f} MB")
        print(f"⏱️ Duration    : {duration} seconds")

if __name__ == "__main__":
    print("🎬 YouTube Video Downloader")
    video_url = input("📎 Paste YouTube video URL: ")
    download_video(video_url)
