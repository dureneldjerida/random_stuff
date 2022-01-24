import os
from pytube import YouTube
from moviepy.editor import *
import sys

os.chdir("D:/Unprocessed Music/")
print(f"Changing directory to {os.getcwd()}\n\n")

with open("videos.txt", "r") as f:
    videos = f.readlines()

for x in videos:
    x.replace("\n", ".")
    yt = YouTube(str(x))
    video = yt.streams.filter().first().download()
    base, ext = os.path.splitext(video)
    new_file = base + '.mp3'
    with VideoFileClip(video) as v:
        with v.audio as a:
            a.write_audiofile(new_file)
    print(f"{yt.title} has been successfully downloaded")
    sys.exit

#https://pytube.io/en/latest/user/streams.html#filtering-streams