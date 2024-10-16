import tkinter as tk
import threading
import pyautogui
import time
import keyboard
from PIL import Image, ImageTk

clicking = False
running = True

def quit_me(root_window):
    global running
    running = False
    root_window.quit()
    root_window.destroy()

def start_clicking():
    global clicking
    clicking = True
    clicking_thread = threading.Thread(target=click_loop)
    clicking_thread.start()

def stop_clicking():
    global clicking
    clicking = False

def click_loop():
    interval = float(entry.get())
    while clicking:
        pyautogui.click()
        time.sleep(interval)

def hotkey_listener():
    while running:
        if keyboard.is_pressed("F7"):
            start_clicking()
        elif keyboard.is_pressed("F8"):
            stop_clicking()
        time.sleep(0.1)

# --- GUIの設定 ---
root = tk.Tk()
root.title("SOVIET AUTO CLICKER")
root.protocol("WM_DELETE_WINDOW", lambda: quit_me(root))
root.geometry("300x300")
root.resizable(False, False)


# 背景画像の設定
image = Image.open("background.png")
resized_image = image.resize((300, 300), Image.Resampling.LANCZOS)
background_image = ImageTk.PhotoImage(resized_image)

background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# タイトルラベル(ソ連スタイルのフォントと金と赤の色を使用)
title_label = tk.Label(root, text="КЛИКЕР", font=("Helvetica", 20, "bold"), fg="#FFD700", bg="#800000")
title_label.pack(pady=10)

# 説明ラベル(現時点では英語)(後日変更する可能性有り)
label = tk.Label(root, text="Enter click interval (seconds):", font=("Helvetica", 12), fg="white", bg="#800000")
label.pack()

# ホットキーショートカットの説明
keyLabel = tk.Label(root, text="F7: Start clicking\nF8: Stop clicking", font=("Helvetica", 10), fg="white", bg="#800000")
keyLabel.pack(pady=5)

# クリック間隔の入力フィールド
entry = tk.Entry(root, font=("Helvetica", 12), justify='center', fg="#FFD700", bg="#333333")
entry.insert(0, "0.5")
entry.pack(pady=5)

# ボタンデザイン(ソ連風、金と赤を使用)
start_button = tk.Button(root, text="Start", font=("Helvetica", 12, "bold"), fg="#800000", bg="#FFD700", command=start_clicking)
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop", font=("Helvetica", 12, "bold"), fg="#800000", bg="#FFD700", command=stop_clicking)
stop_button.pack(pady=5)

# ホットキーリスナーを別スレッドで実行する
hotkey_thread = threading.Thread(target=hotkey_listener)
hotkey_thread.start()

root.mainloop()
