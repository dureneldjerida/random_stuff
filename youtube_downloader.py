import os
import sys
import json
import youtube_dl

if __name__ == "__main__":
    x = input("YOU ARE STARTING THIS PROGRAM ARE YOU SURE YOU WANT TO START [y/n]: ")
    if x == "yes" or x == "y":
        pass
    else:
        print("STOPPING PROGRAM...")
        exit()


data = json.load(open('path.json', 'r'))

os.chdir(data.get("music_dir"))
print(f"\nChanging directory to {os.getcwd()}...")

ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }
try:
    i = input("Please input the url of the playlist/video you would like to download\n>> ")

    if i.startswith("https://www.youtube.com/") == False:
        raise Exception("Not a youtube url.")
    else:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([i])
except Exception:
    sys.exc_clear()