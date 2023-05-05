import tkinter as tk
import ttkbootstrap as ttk
from os import path
from tkinter import PhotoImage, Canvas
from Scripts.Credentials.firstTime import signup 
from Scripts.gradientFrame import GradientFrame
from firstTime import USER_THEMES


def credential():
    if path.exists("Scripts\Credentials\Credentials.json"):
        signup()
    else:
        pass

class App(ttk.Window):
    def __init__(self):
        super().__init__()
        ## == SETTINGS == ##
        # ttkbootstrap style
        style = ttk.Style(theme="firsttime")
        window = style.master

        # centering Window
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()

        x = (ws/2) - 200
        x = round(x)
        y = (hs/2) - 200
        y = round(y)

        # Windows settings
        self.geometry(f"{400}x{400}+{x}+{y}")
        self.overrideredirect(True)
        self.configure(bg="#856ff8")

        # Creating Containter
        background = PhotoImage(file =r"Assets\\background.png")
        self.background = background
        containter = ttk.Frame(self)

        ## == ALL WIDGETS == ##
        # background
        #bgcanvas =  ttk.Canvas(self,
        #                    width=400,
        #                    height=400,
        #                    bd=0,
        #                    highlightthickness=0,)
#
        #bgcanvas.pack(fill = "both", expand=True)
        #
        #background = PhotoImage(file =r"Assets\\background.png")
        #self.background = background
        #
        ## background Image
        #bgcanvas.create_image((0, 0), image=background, anchor = "nw")
#
        ## Title text
        #miniHeader = "this is a sign-up"
        #mainHeader = "Welcome in PeriCait"
        #infoHeader1 = "When you first start this app, we need" 
        #infoHeader2 = "some info to display right informations!"
#
        #bgcanvas.create_text(200, 30, text=miniHeader, fill="#C8AA6E", font=("Beaufort for LOL", 14), width=380)
        #bgcanvas.create_text(200, 70, text=mainHeader, fill="#F0E6D2", font=("Beaufort for LOL", 28), width=380)
        #bgcanvas.create_text(200, 120, text=infoHeader1, fill="#A09B8C", font=("Spiegel Regular", 12), width=380)
        #bgcanvas.create_text(200, 140, text=infoHeader2, fill="#A09B8C", font=("Spiegel Regular", 12), width=380)
        #bgcanvas.pack()
#
        ## Region select
        #regions= ["EUNE", "EUW", "BR", "LAN", "LAS", "NA", "OCE", "RU", "TR", "JP", "KR", "PH", "SG", "TW", "TH", "VN"]
        #currentVar = ttk.StringVar()
        #regionSelector = ttk.Combobox(bgcanvas, width= 30, textvariable= currentVar, values=regions)
        #regionSelector.pack(pady=170, expand="yes")
#
        ## Summoner name select
        #summonerEntry = ttk.Entry(bgcanvas, width=30, textvariable="Your summoner name")
        #summonerEntry.pack(pady=0, expand="yes")

if __name__ == "__main__":
    credential()
    window = App()
    window.mainloop()
