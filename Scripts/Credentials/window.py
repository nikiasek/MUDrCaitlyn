import tkinter as tk
import ttkbootstrap as tkb
import json
import requests
import time

class App(tkb.Window):
        def __init__(self):
                super().__init__()
                ## ======================================================== SETTINGS ======================================================== ##
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

                ## ======================================================== Values ======================================================== ## 
                # background image
                background = tk.PhotoImage(file =r"Assets\\background.png")
                self.background = background

                # Continue Button
                continueButtonImage = tk.PhotoImage(file=r"Assets\\Credentials\\continueButton.png")
                self.continueButtonImage = continueButtonImage

                # Toplevel okay button
                okayButtonImage = tk.PhotoImage(file=r"Assets\\topCredentials\\okayButton.png")
                self.okayButtonImage = okayButtonImage

                # Region selector - regions
                regions= ["EUNE", "EUW", "BR", "LAN", "LAS", "NA", "OCE", "RU", "TR", "JP", "KR", "PH", "SG", "TW", "TH", "VN"]
                regionVar = tkb.StringVar()

                # Text fuck - texts
                miniHeader = "this is a sign-up"
                mainHeader = "Welcome in PeriCait"
                infoHeader = "When you first start this app, we need some info to display right informations!" 
                regionHeader = "Select your region!"
                summonerHeader = "type your summoner name!"

                # Toplevel fuck - texts
                topMiniHeader = "this is a sign-up"
                topMainHeader = "Something went wrong"
                topInfoHeader = "You selected wrong region or typed wrong summoner name, please try again"

                # Summoner name - value
                summonerVar = tkb.StringVar()

                ## ======================================================== LOGIC ======================================================== ## 
                def callback():          
                        current_region = regionVar.get()
                        current_summoner = summonerVar.get()
                        api_key = ""
                        regionJSON = json.load(open("Scripts\\regions.json"))
                        regionlol = (regionJSON[current_region])
                        idiot = requests.get("https://" + regionlol + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + current_summoner + "?api_key=" + api_key)
                        if idiot.status_code == 200:
                                credentials = {"name": current_summoner,
                                        "region": current_region}
                                with open("Scripts\Credentials\credentials.json", "w") as x:
                                        json.dump(credentials, x)
                                self.destroy()
                                self.update()
                                import Scripts.Application.window
                        else:
                                pass

                def popup():
                        ## ============================== POPUP SETTINGS ============================== ##
                        top = tkb.Toplevel(self)
                        top.geometry(f"{resolution[0]}x{resolution[1]}+{x}+{y}")
                        top.title("KOKOT")
                        top.background = background
                        top.overrideredirect(True)

                        ## ============================== POPUP LOGIC ============================== ##
                        def topExitButton():
                                top.destroy()
                                top.update()
                        
                        ## ============================== POPUP STYLING ============================== ##
                        # background - canvas
                        topCanvas = tkb.Canvas(top, width=resolution[0], height=resolution[1], bd=0, highlightthickness=0)
                        topCanvas.create_image((0, 0), image=background, anchor = "nw")

                        # background - text fuck
                        topCanvas.create_text(200, 30, text=topMiniHeader, fill="#C8AA6E", font=("Beaufort for LOL", 14), width=380)
                        topCanvas.create_text(200, 70, text=topMainHeader, fill="#F0E6D2", font=("Beaufort for LOL", 28), width=380)
                        topCanvas.create_text(200, 120, text=topInfoHeader, fill="#A09B8C", font=("Spiegel Regular", 12), width=380, justify="center")
                        topCanvas.pack()

                        # Frames
                        okayButtonFrame = tkb.Frame(topCanvas)
                        topCanvas.create_window(200, 190, window=okayButtonFrame)

                        # exit Button
                        okayButton = tk.Button(master= okayButtonFrame, image=okayButtonImage, command=topExitButton)
                        okayButton.pack()

                ## ====================================================== STYLING ======================================================== ##
                # background - canvas
                bgcanvas =  tkb.Canvas(self, width=resolution[0], height=resolution[1], bd=0, highlightthickness=0)

                # background - Image
                bgcanvas.create_image((0, 0), image=background, anchor = "nw")

                # Text fuck - labels
                bgcanvas.create_text(200, 30, text=miniHeader, fill="#C8AA6E", font=("Beaufort for LOL", 14), width=380)
                bgcanvas.create_text(200, 70, text=mainHeader, fill="#F0E6D2", font=("Beaufort for LOL", 28), width=380)
                bgcanvas.create_text(200, 120, text=infoHeader, fill="#A09B8C", font=("Spiegel Regular", 12), width=380, justify="center")
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


                # Region selector - combobox
                regionCombobox = tkb.Combobox(master= regionFrame, width=30, values=regions, textvariable=regionVar)
                regionCombobox.pack()

                # Summoner name
                summonerEntry = tkb.Entry(master= summonerFrame, width=32, textvariable=summonerVar)
                summonerEntry.pack()

                # Continue Button
                continueButton = tk.Button(master= buttonFrame, image=continueButtonImage, command=callback)
                continueButton.pack()

if __name__ == "Scripts.Credentials.window":
        window = App()
        window.mainloop()