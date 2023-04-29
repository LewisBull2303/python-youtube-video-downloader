from pytube import YouTube
from sys import argv
import os

yt = YouTube(str(input("Enter the URL of the video that you wish to download: ")))

video = yt.streams.get_highest_resolution()

out_file = video.download(output_path="C:\Python projects\Songs and videos\svideos")

base, ext = os.path.splitext(out_file)
new_file = base + '.mp4'
os.rename(out_file, new_file)

print(yt.title + " has been successfully downloaded.")