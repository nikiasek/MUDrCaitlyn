import tkinter as tk
import ttkbootstrap as tkb

class App(tkb.Window):
        def __init__(self):
                super().__init__()
                # centering Window
                ws = self.winfo_screenwidth()
                hs = self.winfo_screenheight()
                x = round((ws/2) - 200)
                y = round((hs/2) - 200)
                resolution = (400, 400)

                # Window setings
                self.geometry(f"{resolution[0]}x{resolution[1]}+{x}+{y}")
                self.overrideredirect(True)
                style = tkb.Style(theme="firsttime")
                #self.config(highlightbackground="#2b3e50")
                #self.wm_attributes('-transparentcolor', "#2b3e50")
                ## == STYLING == ##
                # background - canvas
                bgcanvas =  tkb.Canvas(self, width=resolution[0], height=resolution[1], bd=0, highlightthickness=0)
                background = tk.PhotoImage(file =r"Assets\\background.png")
                self.background = background

                # background - Image
                bgcanvas.create_image((0, 0), image=background, anchor = "nw")

                # Text fuck - texts
                miniHeader = "this is a sign-up"
                mainHeader = "Welcome in PeriCait"
                infoHeader = "When you first start this app, we need\nsome info to display right informations!" 
                regionHeader = "Select your region!"
                summonerHeader = "type your summoner name!"

                # Text fuck - labels
                bgcanvas.create_text(200, 30, text=miniHeader, fill="#C8AA6E", font=("Beaufort for LOL", 14), width=380)
                bgcanvas.create_text(200, 70, text=mainHeader, fill="#F0E6D2", font=("Beaufort for LOL", 28), width=380)
                bgcanvas.create_text(200, 120, text=infoHeader, fill="#A09B8C", font=("Spiegel Regular", 12), width=380)
                bgcanvas.create_text(200, 160, text=regionHeader, fill="#C8AA6E", font=("Spiegel Regular", 12), width=380)
                bgcanvas.create_text(200, 230, text=summonerHeader, fill="#C8AA6E", font=("Spiegel Regular", 12), width=380)
                bgcanvas.pack()

                # Frames
                regionFrame = tk.Frame(bgcanvas)             
                summonerFrame = tk.Frame(bgcanvas) 
                buttonFrame = tk.Frame(bgcanvas)
                bgcanvas.create_window(200, 190, window=regionFrame)
                bgcanvas.create_window(200, 260, window=summonerFrame)
                bgcanvas.create_window(200, 320, window=buttonFrame)

                # Region selector - regions
                regions= ["EUNE", "EUW", "BR", "LAN", "LAS", "NA", "OCE", "RU", "TR", "JP", "KR", "PH", "SG", "TW", "TH", "VN"]
                currentVar = tkb.StringVar()

                # Region selector - combobox
                regionCombobox = tkb.Combobox(master= regionFrame, width=30, values=regions, textvariable=currentVar)
                regionCombobox.pack()

                # Summoner name
                summonerEntry = tkb.Entry(master= summonerFrame, width=32)
                summonerEntry.pack()

                # Continue Button
                continueButtonImage = tk.PhotoImage(file=r"Assets\\continueButton.png")
                self.continueButtonImage = continueButtonImage
                continueButton = tk.Button(master= buttonFrame, image=continueButtonImage)
                continueButton.pack()
                

if __name__ == "__main__":
        window = App()
        window.mainloop()