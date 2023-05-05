import tkinter as tk
import ttkbootstrap as tkb

class App(tkb.Window):
        def __init__(self):
                super().__init__()
                # centering Window
                ws = self.winfo_screenwidth()
                hs = self.winfo_screenheight()
                x = (ws/2) - 200
                x = round(x)
                y = (hs/2) - 200
                y = round(y)

                # Window setings
                self.geometry(f"{400}x{400}+{x}+{y}")
                #self.overrideredirect(True)
                self.configure(bg="#303030")
                style = tkb.Style(theme="firsttime")
                window = style.master

                ## == STYLING == ##
                # background - canvas
                bgcanvas =  tkb.Canvas(self, width=400, height=400, bd=0, highlightthickness=0,)
                bgcanvas.pack(fill = "both", expand=True)
                background = tk.PhotoImage(file =r"Assets\\background.png")
                self.background = background

                # background - Image
                bgcanvas.create_image((0, 0), image=background, anchor = "nw")
#
                # Frame

                # Text fuck - texts
                miniHeader = "this is a sign-up"
                mainHeader = "Welcome in PeriCait"
                infoHeader1 = "When you first start this app, we need" 
                infoHeader2 = "some info to display right informations!"
                
                # Text fuck - labels

                bgcanvas.create_text(200, 30, text=miniHeader, fill="#C8AA6E", font=("Beaufort for LOL", 14), width=380)
                bgcanvas.create_text(200, 70, text=mainHeader, fill="#F0E6D2", font=("Beaufort for LOL", 28), width=380)
                bgcanvas.create_text(200, 110, text=infoHeader1, fill="#A09B8C", font=("Spiegel Regular", 12), width=380)
                bgcanvas.create_text(200, 130, text=infoHeader2, fill="#A09B8C", font=("Spiegel Regular", 12), width=380)

                # Region selector - regions
                regions= ["EUNE", "EUW", "BR", "LAN", "LAS", "NA", "OCE", "RU", "TR", "JP", "KR", "PH", "SG", "TW", "TH", "VN"]
                currentVar = tkb.StringVar()

                # Region selector - combobox
                regionCombobox = tkb.Combobox(bgcanvas, width=30, values=regions, textvariable=currentVar)
                regionCombobox.pack(pady=160)

                # Summoner name

                summonerEntry = tkb.Entry(bgcanvas, width=30, textvariable="Your summoner name")
                summonerEntry.pack(pady=100)

if __name__ == "__main__":
        window = App()
        window.mainloop()