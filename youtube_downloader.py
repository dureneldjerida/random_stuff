import os
import sys
<<<<<<< HEAD
import json
import youtube_dl

if __name__ == "__main__":
    x = input("YOU ARE STARTING THIS PROGRAM ARE YOU SURE YOU WANT TO START [y/n]: ")
    if x == "yes" or x == "y":
        pass
    else:
        print("STOPPING PROGRAM...")
        exit()
=======
from tqdm import tqdm

os.chdir("/Users/aaatipamula/Desktop/unprocessed_music/")
print(f"\nChanging directory to {os.getcwd()}")
>>>>>>> fa302964e416f8428f1e66636396150b9f24459d


<<<<<<< HEAD
data = json.load(open('path.json', 'r'))
=======
for x in videos:
    x.replace("\n", ".")
    os.chdir("/Users/aaatipamula/Desktop/unprocessed_music/videos_downloaded/")
    print(f"Changing directory to {os.getcwd()}")
    yt = YouTube(str(x))
    for i in tqdm(range(100)):
        video = yt.streams.filter(file_extension = 'mp4', res= '1080p').first().download(output_path= "/Users/aaatipamula/Desktop/unprocessed_music/videos_downloaded/")
    print(f"{yt.title}.mp4 downloaded")
    os.chdir("/Users/aaatipamula/Desktop/unprocessed_music/music_downloaded/")
    print(f"Changing directory to {os.getcwd()}")
    outfile = os.path.split(video)
    outfile
    with VideoFileClip(video) as v:
        with v.audio as a:
            a.write_audiofile(outfile)
    print(f"{yt.title} is downloaded and converted!\n")
    sys.exit
>>>>>>> fa302964e416f8428f1e66636396150b9f24459d

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