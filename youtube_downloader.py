import os
from pytube import YouTube

os.chdir("D:/Unprocessed Music/")
print(f"\n\nChanging directory to {os.getcwd()}\n\n")

with open("videos.txt", "r") as f:
    videos = f.readlines()

for x in videos:
    x.replace("\n", ".")
    yt = YouTube(str(x))
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(f"{yt.title} has been successfully downloaded")