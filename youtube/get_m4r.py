import yt_dlp
from pydub import AudioSegment

url = input("URL:")
file_name = input("File Name:")

ydl_opts = {
    'format': 'bestaudio',
    'outtmpl': f'{file_name}.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

mp3_audio = AudioSegment.from_mp3(f'{file_name}.mp3')
mp3_audio.export(f"{file_name}.m4r", format="mp4")
