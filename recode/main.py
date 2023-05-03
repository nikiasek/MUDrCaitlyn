import tkinter as tk
import ttkbootstrap as ttk
from os import path
from MUDrCaitlyn.recode.Credentials.firstTime import signup 


def credential():
    if path.exists("recode\Scripts\Credentials\Credentials.json"):
        ft()
    else:
        pass


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # Windows settings
        self.geometry(f"{1280}x{720}")
        self.title("Professor Caitlyn")
        self.iconbitmap("Recode\Caitlyn.ico")



if __name__ == "__main__":
    credential()
    window = App()
    window.mainloop()
