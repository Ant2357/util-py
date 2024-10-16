import tkinter as tk
import threading
import pyautogui
import time
import keyboard

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

root = tk.Tk()
root.title("クリック連打ツール")
root.protocol("WM_DELETE_WINDOW", lambda :quit_me(root))
root.geometry("200x135")

label = tk.Label(root, text="クリックの間隔(秒)を入力:")
label.pack()

keyLabel = tk.Label(root, text="F7: クリック開始\nF8: クリック停止")
keyLabel.pack()

entry = tk.Entry(root)
entry.pack()


start_button = tk.Button(root, text="開始", command=start_clicking)
start_button.pack()

stop_button = tk.Button(root, text="停止", command=stop_clicking)
stop_button.pack()

hotkey_thread = threading.Thread(target=hotkey_listener)
hotkey_thread.start()

root.mainloop()
