import tkinter as tk
import threading
import time
import keyboard
from PIL import Image, ImageTk

class AutoClickerGUI:
    def __init__(self, root, clicker) -> None:
        self.root = root
        self.clicker = clicker
        self.running = True

        root.title("SOVIET AUTO CLICKER")
        root.protocol("WM_DELETE_WINDOW", self.quit_me)
        root.geometry("300x300")
        root.resizable(False, False)

        # 背景画像の設定
        image = Image.open("./assets/images/background.png")
        resized_image = image.resize((300, 300), Image.Resampling.LANCZOS)
        self.background_image = ImageTk.PhotoImage(resized_image)
        background_label = tk.Label(root, image=self.background_image)

        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # タイトルラベル(ソ連スタイルのフォントと金と赤の色を使用)
        title_label = tk.Label(root, text="КЛИКЕР", font=("Helvetica", 20, "bold"), fg="#FFD700", bg="#800000")
        title_label.pack(pady=10)

        # 説明ラベル(現時点では英語)(後日変更する可能性有り)
        label = tk.Label(root, text="Enter click interval (seconds):", font=("Helvetica", 12), fg="#FFD700", bg="#800000")
        label.pack()

        # ホットキーショートカットの説明
        keyLabel = tk.Label(root, text="F7: Start clicking\nF8: Stop clicking", font=("Helvetica", 10, "bold"), fg="#FFD700", bg="#800000")
        keyLabel.pack(pady=5)

        # クリック間隔の入力フィールド
        self.entry = tk.Entry(root, font=("Helvetica", 12), justify='center', fg="#FFD700", bg="#333333")
        self.entry.insert(0, "0.5")
        self.entry.pack(pady=5)

        # ボタンデザイン(ソ連風、金と赤を使用)
        start_button = tk.Button(root, text="Start", font=("Helvetica", 12, "bold"), fg="#800000", bg="#FFD700", command=self.start_clicking)
        start_button.pack(pady=5)

        stop_button = tk.Button(root, text="Stop", font=("Helvetica", 12, "bold"), fg="#800000", bg="#FFD700", command=self.stop_clicking)
        stop_button.pack(pady=5)

        # ホットキーリスナーをスレッドで実行する
        hotkey_thread = threading.Thread(target=self.hotkey_listener)
        hotkey_thread.start()


    def start_clicking(self) -> None:
        self.clicker.click_interval = float(self.entry.get())
        self.clicker.start_clicking()

    def stop_clicking(self) -> None:
        self.clicker.stop_clicking()

    def hotkey_listener(self) -> None:
        while self.running:
            if keyboard.is_pressed("F7"):
                self.clicker.start_clicking()
            elif keyboard.is_pressed("F8"):
                self.clicker.stop_clicking()
            time.sleep(0.1)

    def quit_me(self) -> None:
        self.running = False
        self.clicker.stop_clicking()
        self.root.quit()
        self.root.destroy()
