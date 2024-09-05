import yt_dlp
from pydub import AudioSegment

url = input("URL:")

ydl_opts = {
    'format': 'bestaudio',
    'outtmpl':'output.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

mp3_audio = AudioSegment.from_mp3('output.mp3')
mp3_audio.export("output.m4r", format="mp4")
