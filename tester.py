# importing packages
from pytube import YouTube
import os

os.chdir("/Users/aaatipamula/Desktop/unprocessed_music/")

with open("videos.txt", "r") as f:
    video = f.readline() 

# url input from user
yt = YouTube(str(video))
  
# extract only audio
v = yt.streams.filter(file_extension = 'mp4', res= '1080p').first().download()
x = v.split("unprocessed_music/")

print(v)
print(x)