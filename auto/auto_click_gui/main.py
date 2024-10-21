import tkinter as tk

import clicker
import auto_clicker_gui

if __name__ == "__main__":
    clicker = clicker.Clicker(0.5)
    root = tk.Tk()
    gui = auto_clicker_gui.AutoClickerGUI(root, clicker)
    root.mainloop()
