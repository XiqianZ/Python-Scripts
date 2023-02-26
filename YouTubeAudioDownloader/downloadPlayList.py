from pytube import Playlist
from pytube import YouTube
from pydub import AudioSegment
import os
import regex as re

def download_playlist(playlist_url):
    playlist = Playlist(playlist_url)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    for url in playlist.video_urls:
        yt = YouTube(f"https://youtube.com{url}")
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download()

    print(f"{yt.title} downloaded and converted successfully")

playlist_url = "https://youtube.com/playlist?list=PLF6H9dGMv1K_HIQYWkv4VCeYVx5wa4iqS"
download_playlist(playlist_url)