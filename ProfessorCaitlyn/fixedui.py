import tkinter as tk
import customtkinter as ctk
import json
import requests
import shutil
from pathlib import Path
from PIL import ImageTk,Image


#START
championslist = Path("championslist.json")
if championslist.is_file():
    print("championslist founded")
else:
    champions = requests.get("http://ddragon.leagueoflegends.com/cdn/12.20.1/data/en_US/champion.json")
    champions = champions.json()
    with open("championslist.json", "w") as outfile:
       json.dump(champions, outfile, indent=1)

championlist = list()

#CHAMP LIST
champslist = open ("championslist.json", "r")
champslist = json.loads(champslist.read())
for champs in champslist["data"]:
    championlist.append(champs)


#DATA CALLBACK
def data_callback(choice):
    ChampsJSON = requests.get("http://ddragon.leagueoflegends.com/cdn/12.20.1/data/en_US/champion/" + choice + ".json")
    ChampsJSON = ChampsJSON.json() 
    #IMAGES
    passive = (ChampsJSON["data"][choice]["passive"]["image"]["full"])
    passivepath = Path(passive)
    #Passive request
    if passivepath.is_file():
        print("passive exists")
    else:
        passiverequest = requests.get("http://ddragon.leagueoflegends.com/cdn/12.20.1/img/passive/" + passive, stream = True)
        if passiverequest.status_code == 200:
            with open(passive, "wb") as p:
               shutil.copyfileobj(passiverequest.raw, p)
        else:
            print("something went wrong")
    #Ability request
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
    #Loading art request
    loading_art = (choice + "_0.jpg")
    loading_art_path = Path(loading_art)
    if loading_art_path.is_file():
        print(loading_art + "exist")
    else:
        loading_art_request = requests.get("http://ddragon.leagueoflegends.com/cdn/img/champion/loading/" + loading_art, stream = True)
        if loading_art_request.status_code == 200:
            with open(loading_art, "wb") as a:
                shutil.copyfileobj(loading_art_request.raw, a)
    #IMAGESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS


# === MAIN WINDOW ===
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        

        self.geometry(f"{1280}x{720}")
        self.title("Professor Caitlyn")
        self.iconbitmap("Caitlyn.ico")
        self.resizable(False, False)

        # === left frame ===sssssssss

        self.left_frame = ctk.CTkFrame(master=self,
                                        width=250,
                                        height=700,
                                        corner_radius=10)
        self.left_frame.place(x=10, y=10)

        # === abilities frame ===

        self.abilities_frame = ctk.CTkFrame(master=self,
                                            width= 390,
                                            height= 84,
                                            corner_radius=10)
        self.abilities_frame.place(x=270, y=10)

        # === Choose menu default variable ===
        
        self.optionmenu_var = ctk.StringVar(value="Choose")

        # === Choose menu ===

        self.combobox = ctk.CTkComboBox(master=self,
                                        values= championlist,
                                        command=data_callback,
                                        variable=self.optionmenu_var,
                                        width=230)
        self.combobox.place(x=20, y=20)

        # === Passive button ===

        

        self.passive_button = ctk.CTkButton(master=self,
                                            text="",
                                            image=App.p_image,
                                            fg_color=("#2a2d2e"),
                                            width=64,
                                            height=64)
        self.passive_button.place(x=280, y=18)

        # === Q button ===

        self.q_button = ctk.CTkButton(master=self,
                                            text="Pas",
                                            width=64,
                                            height=64)
        self.q_button.place(x=354, y=20)

        # === W button ===

        self.w_button = ctk.CTkButton(master=self,
                                            text="Pas",
                                            width=64,
                                            height=64)
        self.w_button.place(x=428, y=20)

        # === E button ===

        self.e_button = ctk.CTkButton(master=self,
                                            text="Pas",
                                            width=64,
                                            height=64)
        self.e_button.place(x=502, y=20)

        # === R button ===

        self.r_button = ctk.CTkButton(master=self,
                                            text="Pas",
                                            width=64,
                                            height=64)
        self.r_button.place(x=576, y=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()