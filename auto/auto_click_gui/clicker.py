import threading
import pyautogui
import time

class Clicker:
    def __init__(self, interval) -> None:
        self.clicking = False
        self.interval = interval

    def start_clicking(self) -> None:
        self.clicking = True
        clicking_thread = threading.Thread(target=self.click_loop)
        clicking_thread.start()

    def stop_clicking(self) -> None:
        self.clicking = False

    def click_loop(self) -> None:
        while self.clicking:
            pyautogui.click()
            time.sleep(self.interval)

    def set_interval(self, interval) -> None:
        self.interval = interval
