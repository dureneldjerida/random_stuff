import os
from pytube import YouTube
from moviepy.editor import *
import sys
from tqdm import tqdm

os.chdir("/Users/aaatipamula/Desktop/unprocessed_music/")
print(f"\nChanging directory to {os.getcwd()}")

with open("videos.txt", "r") as f:
    videos = f.readlines()

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

#https://pytube.io/en/latest/user/streams.html#filtering-streams