import os
from pytube import YouTube
from moviepy.editor import *
import sys
from tqdm import tqdm
import json

data = json.load(open('path.json', 'r'))

os.chdir(data.get("music_dir"))
print(f"Changing directory to {os.getcwd()}...")

with open("videos.txt", "r") as f:
    videos = f.readlines()

for x in videos:
    x.replace("\n", ".")

    yt = YouTube(str(x))

    print("Downloading video...")
    for i in tqdm(range(100)):
        video = yt.streams.filter(file_extension = 'mp4').get_highest_resolution().download(output_path= data.get("video_dir"))
    print(f"{yt.title}.mp4 downloaded.")

    print("Downloading audio...")
    for i in tqdm(range(100)):
        audiofile = yt.streams.filter(only_audio= True, abr= "128kbps").first().download()
    print(f"{yt.title} audio downloaded.")

    outfile = audiofile.replace("mp4", "mp3")

    with AudioFileClip(audiofile) as a:
        a.write_audiofile(outfile)

    os.remove(audiofile)

    print(f"{yt.title} is downloaded and converted!\n")
