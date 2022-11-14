import pyautogui as autogui
import tkinter as tk
from tkinter import ttk


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    print(B1)
    popup.mainloop()


number_of_animals = (0,0)
dog_position = (0,0)
sexe_female_position = (0,0)
sexe_male_position = (0,0)
castrer_non_position = (0,0)
castrer_oui_position = (0,0)
position_race_text_box = (0,0)
position_peu_actif = (0,0)
position_moyen_actif = (0,0)
position_tres_actif = (0,0)
position_peu_maigre = (0,0)
position_ideal_corps = (0,0)
position_gros_coprs = (0,0)
position_type_de_croquette = (0,0)
position_test_menu = (0,0)
position_finaliser = (0,0)
position_vrai_prix = (0,0)

variables = {
    "number_of_animals" : number_of_animals,
    "dog_position": dog_position,
    "sexe_female_position" :sexe_female_position,
    "sexe_male_position": sexe_male_position,
    "castrer_non_position" :castrer_non_position,
    "castrer_oui_position" : castrer_oui_position, 
    "position_race_text_box" : position_race_text_box,
    "position_peu_actif" : position_peu_actif,
    "position_moyen_actif" : position_moyen_actif,
    "position_tres_actif" : position_tres_actif,
    "position_peu_maigre" : position_peu_maigre,
    "position_ideal_corps": position_ideal_corps,
    "position_gros_coprs": position_gros_coprs, 
    "position_type_de_croquette": position_type_de_croquette,
    "position_test_menu" : position_test_menu,
    "position_finaliser" : position_finaliser, 
    "position_vrai_prix" : position_vrai_prix}