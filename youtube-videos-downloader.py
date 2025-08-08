from pytube import YouTube
import os

link = input("Enter YouTube video URL: ")
yt = YouTube(link)

video = yt.streams.get_highest_resolution()

save_path = input("Enter folder path to save the video (leave empty for current folder): ")
if save_path.strip() == "C:/Users/ilyass/Desktop/video":
    save_path = os.getcwd()

print("Downloading...")
video.download(output_path=save_path)
print("✅ Downloaded to", save_path)