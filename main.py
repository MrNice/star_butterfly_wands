# This is a sample Python script. import vlc

import vlc
import tkinter as tk

from tkinter import ttk

from collections import deque


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.instance = vlc.Instance()
        self.pack()
        self.create_widgets()
        self.media = self.instance.media_new(r"/home/pixel/videos/sample-5s.mp4")
        self.media2 = self.instance.media_new(r"/home/pixel/videos/sample-30s.mp4")
        self.media_queue = deque()
        self.media_queue.append(self.media)
        self.media_queue.append(self.media2)
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
