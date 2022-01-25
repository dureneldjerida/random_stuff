import os
import sys
import json
import yt_dlp

data = json.load(open('setup.json', 'r'))

opt1 = ["yes", "y"]
opt2 = ["no", "n"]

selector_txt = "\nPlease enter what format you would like to download in...\nInput 1 for audio only, 2 for video, 3 for both.\n>> "

def start():
    while True:
        x = input("YOU ARE STARTING THIS PROGRAM ARE YOU SURE YOU WANT TO START [y/n]: ")
        if x.lower() in opt1:
            break
        elif x.lower() in opt2:
            print("STOPPING PROGRAM...")
            exit()
        else:
            print("Please enter a valid option.")

        
def music_download():
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
        while True: 
            i = input("Please input the url of the playlist/video you would like to download\n>> ")
            if i.startswith("https://www.youtube.com/"):
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([i]) 
            else:
                raise Exception("Not a youtube url.")
    except Exception:
        sys.exc_clear()

def video_download():
    os.chdir(data.get("video_dir"))
    print(f"\nChanging directory to {os.getcwd()}...")

    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s'
    }
    try:
        while True: 
            i = input("Please input the url of the playlist/video you would like to download\n>> ")
            if i.startswith("https://www.youtube.com/"):
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([i]) 
            else:
                raise Exception("Not a youtube url.")
    except Exception:
        sys.exc_clear()

def both():
    music_download()
    video_download()

def selector():
    key = {
        "1":music_download(),
        "2":video_download(),
        "3":both(),
    }
    while True:
        x = input(selector_txt)
        if x in key:
            key.get(x)  
        else:
            print("Please enter a valid option.")   

if __name__ == "__main__":
    start()
    selector()
    