import tkinter as tk
from tkinter import messagebox
import threading
import yt_dlp
from pydub import AudioSegment

class SimpleDownloader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Audio Downloader")
        self.geometry('400x200')
        self.resizable(False, False)

        # YouTube URL の入力欄
        tk.Label(self, text='YouTube URL:').pack(pady=(20, 5), padx=20, anchor='w')
        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.pack(padx=20)

        # ファイル名の入力欄
        tk.Label(self, text='Save As (without extension):').pack(pady=(10, 5), padx=20, anchor='w')
        self.name_entry = tk.Entry(self, width=50)
        self.name_entry.pack(padx=20)

        # ダウンロードボタン(mp3・m4r)
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=15)

        mp3_btn = tk.Button(btn_frame, text='Download MP3', width=15,
                            command=lambda: threading.Thread(target=self.download, args=('mp3',)).start())
        mp3_btn.pack(side='left', padx=10)

        m4r_btn = tk.Button(btn_frame, text='Download M4R', width=15,
                            command=lambda: threading.Thread(target=self.download, args=('m4r',)).start())
        m4r_btn.pack(side='left', padx=10)

        # Status ラベル
        self.status_label = tk.Label(self, text='')
        self.status_label.pack(pady=(0, 10))

    def download(self, fmt):
        url = self.url_entry.get().strip()
        name = self.name_entry.get().strip()
        if not url or not name:
            messagebox.showwarning('Input Error', 'Please enter both URL and file name.')
            return

        self.status_label.config(text='Downloading...')
        try:
            # 現在は yt_dlp を用いて YouTube上から mp3 をダウンロードしている
            ydl_opts = {
                'format': 'bestaudio',
                'outtmpl': f'{name}.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'quiet': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.status_label.config(text='MP3 downloaded.')

            if fmt == 'm4r':
                self.status_label.config(text='Converting to M4R...')
                mp3_audio = AudioSegment.from_mp3(f'{name}.mp3')
                mp3_audio.export(f"{name}.m4r", format="mp4")
                self.status_label.config(text='M4R conversion complete.')

            messagebox.showinfo('Success', f'File saved as {name}.{fmt}')
        except Exception as e:
            messagebox.showerror('Error', f'An error occurred: {e}')
            self.status_label.config(text='')

if __name__ == '__main__':
    app = SimpleDownloader()
    app.mainloop()
