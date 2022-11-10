import tkinter as tk
import customtkinter as ctk
import champions
import json
import requests
import shutil
from pathlib import Path
from PIL import ImageTk,Image


exec("champions")

goven = list()

#CHAMP LIST
champslist = open ("championslist.json", "r")
champslist = json.loads(champslist.read())
for champs in champslist["data"]:
    goven.append(champs)

#MAIN WINDOW
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{1280}x{720}")
        self.title("Professor Caitlyn")
        self.iconbitmap("Caitlyn.ico")


app = App()

#DEFAULT VALUE
optionmenu_var = ctk.StringVar(value="Choose")  

#CHAMPS JSONS
def optionmenu_callback(choice):
    ChampsJSON = requests.get("http://ddragon.leagueoflegends.com/cdn/12.20.1/data/en_US/champion/" + choice + ".json")
    ChampsJSON = ChampsJSON.json() 
    #IMAGES
    passive = (ChampsJSON["data"][choice]["passive"]["image"]["full"])
    passivepath = Path(passive)
    if passivepath.is_file():
        print("passive exists")
    else:
        passiverequest = requests.get("http://ddragon.leagueoflegends.com/cdn/12.20.1/img/passive/" + passive, stream = True)
        if passiverequest.status_code == 200:
            with open(passive, "wb") as p:
               shutil.copyfileobj(passiverequest.raw, p)
        else:
            print("something went wrong")
    for x in range(0, 4):
        ability = (ChampsJSON["data"][choice]["spells"][x]["image"]["full"])
        abilitypath = Path(ability)
        if abilitypath.is_file():
            print(ability + " exists")
        else:
            abilityrequest = requests.get("http://ddragon.leagueoflegends.com/cdn/12.20.1/img/spell/" +  ability, stream = True)
            if abilityrequest.status_code == 200:
                with open(ability, "wb") as a:
                   shutil.copyfileobj(abilityrequest.raw, a)
            else:
              print("something went wrong")

textPassive = ctk.CTkTextbox(app)
textPassive.grid(row=1, column=1)
textPassive.insert("1.1", "KOKOT")
textPassive.configure(state="disabled")
textPassive.pack(padx=18, pady=30)

PassiveImage = ctk.CTkCanvas(app, width = 64, height = 64)   
PassiveImage.pack(padx=30, pady=123)      
PassiveImage.place(x=100, y=100)
img = tk.PhotoImage(file="Caitlyn.png")      
PassiveImage.create_image(20, 20, image=img)        

frame = ctk.CTkFrame(master=app,
                               width=250,
                               height=700,
                               corner_radius=10)
frame.pack()
frame.place(x=10, y=10)

combobox = ctk.CTkComboBox(master=app,
                                     values= goven,
                                     command=optionmenu_callback,
                                     variable=optionmenu_var,
                                     width=230)                    
combobox.pack(padx=1, pady=10)
combobox.place(x=20, y=20)


app.mainloop()

