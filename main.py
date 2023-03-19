# This is a sample Python script. import vlc
import os
from sys import platform

os.environ['DISPLAY'] = ':0.0'
import tomli
import tkinter as tk
import vlc

from tkinter import ttk

from collections import deque

IS_RASPBERRY_PI = os.uname()[4][:3] == 'arm'

with open("config.toml", "rb") as f:
    config = tomli.load(f)
# Video directory and video list will be different on different machines
# TODO(pixelicious): Update the config file to group directory with video file names.
video_dir = r"C:\Users\Nick\Videos\star_wand"
video_files = config["windows_videos"]
if IS_RASPBERRY_PI:
    video_dir = r"/home/pixel/Videos"
    video_files = config["raspberry_pi_videos"]
elif platform == "linux":
    video_dir = r"/home/pixel/videos"
    video_files = config["virtualbox_videos"]

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.instance = vlc.Instance()
        self.pack()
        self.create_widgets()
        for file in video_files:
            path = os.path.join(video_dir, file)
            self.media_queue.append(self.instance.media_new(path))
        self.media_queue = deque()
        self.player = self.instance.media_player_new()
        self.player_widget = ttk.Frame(master, width=320, height=200)
        self.player_widget.pack(fill='both', expand=True)
        self.player.set_xwindow(self.player_widget.winfo_id())
        self.player.set_fullscreen(True)


    def create_widgets(self):
        self.start_button = tk.Button(self, text="Start", command=self.start)
        self.start_button.pack(side="left")

        self.stop_button = tk.Button(self, text="Stop", command=self.stop)
        self.stop_button.pack(side="right")

        self.next_button = tk.Button(self, text="next", command=self.next)
        self.next_button.pack(side="right")

        self.close_button = tk.Button(self, text="close", command=self.close)
        self.close_button.pack(side="right")

    def shift_queue(self):
        shifted = self.media_queue.popleft()
        self.media_queue.append(shifted)
        return shifted

    def start(self):
        shifted = self.shift_queue()
        self.player.set_media(shifted)
        self.player.play()
        print("player.get_state()")
        print(self.player.get_state())

    def next(self):
        shifted = self.media_queue.popleft()
        self.media_queue.append(shifted)
        self.player.set_media(shifted)
        self.player.play()

    def stop(self):
        self.player.stop()
        print("Stop button clicked!")
        print("player.get_state()")
        print(self.player.get_state())
        print("what was player.get_state()")

    def close(self):
        self.player.stop()
        self.player.release()
        tk.Tk().quit()
        tk.Tk().destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("640x480+100+100")
    app = App(master=root)
    app.mainloop()

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
