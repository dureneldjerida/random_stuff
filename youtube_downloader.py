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

    os.chdir(data.get("video_dir"))
    print(f"Changing directory to {os.getcwd()}...")

    yt = YouTube(str(x))

    for i in tqdm(range(100)):
        video = yt.streams.filter(file_extension = 'mp4', res= '1080p').first().download(output_path= data.get("video_dir"))
    print(f"{yt.title}.mp4 downloaded")

    os.chdir(data.get("music_dir"))
    print(f"Changing directory to {os.getcwd()}...")

    path, file = os.path.split(video)
    outfile = os.getcwd() + file.replace("mp4", "mp3")

    with VideoFileClip(video) as v:
        with v.audio as a:
            a.write_audiofile(outfile)
    print(f"{yt.title} is downloaded and converted!\n")
    sys.exit