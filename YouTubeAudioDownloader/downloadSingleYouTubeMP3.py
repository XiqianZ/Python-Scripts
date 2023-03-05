from pytube import YouTube
import os

DIRECTORY = "/downloaded"

def download_audio(url,output_path=os.path.join(os.getcwd(),DIRECTORY)):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path=output_path)
    print(output_path)
    print("Audio downloaded successfully")
    
def download_video(url,output_path=os.path.join(os.getcwd(),DIRECTORY)):
    video = YouTube(url)
    stream = video.streams.filter(file_extension='mp4').first()
    stream.download(output_path=output_path)
    print(output_path)
    print("Video downloaded successfully")

url = "https://www.youtube.com/watch?v=MphBWtqbk-Q"
download_video(url)
