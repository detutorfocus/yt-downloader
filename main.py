import os
import yt_dlp

url = input("Enter YouTube video URL: ").strip()

os.makedirs("downloads", exist_ok=True)

options = {
    "format": "bestvideo[height<=360]+bestaudio/best[height<=360]",
    "merge_output_format": "mp4",
    "js_runtimes": {
        "deno": {}
    },
    "outtmpl": "downloads/%(title)s.%(ext)s",
}

try:
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

except yt_dlp.utils.DownloadError as e:
    print(f"\nDownload failed:\n{e}")