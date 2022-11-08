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

popupmsg('some string')
print(autogui.position())
number_of_animals = (0,0)
dog_position = (0,0)
sex_position = (0,0)
castrer_position = (0,0)
position_suivant_race = (0,0)
position_suivant_age = (0,0)
position_peu_actif = (0,0)
position_moyen_actif = (0,0)
position_tres_actif = (0,0)
position_peu_maigre = (0,0)
position_ideal_corps = (0,0)
position_gros_coprs = (0,0)
position_suivant_poids = (0,0)
position_type_de_croquette = (0,0)
position_finaliser = (0,0)
position_vrai_prix = (0,0)