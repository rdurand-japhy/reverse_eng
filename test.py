from enum import auto
import urllib3
import pyautogui as autogui
import pyperclip as paper
import time
import webbrowser
import pandas as pd
import csv
import random
import tkinter as tk
from tkinter import ttk
import pickle
from calibration import *
NAME = ''
DOG_MENU = ''

fitness_level = {'lazy' : {'x': position_peu_actif.x, 'y':position_peu_actif.y},
                 'normal' : {'x': position_moyen_actif.x, 'y' : position_moyen_actif.y},
                 'very active' :  {'x': position_tres_actif.x, 'y' : position_tres_actif.y}}

body_type = {'thin' : {'x': position_peu_maigre.x, 'y':position_peu_maigre.y},
             'normal' : {'x': position_ideal_corps.x, 'y' : position_ideal_corps.y},
              'fat' :  {'x': position_gros_coprs.x, 'y' : position_gros_coprs.x}} #we dont body shame here


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    print(B1)
    popup.mainloop()

def get_name():
    with open("names.csv") as f:
        reader = csv.reader(f)
        rows = list(reader)
        name = rows[random.randrange(1,1001,1)]
        NAME = name[0]
        return (name[0])

def tab_presses(number):
    for i in range(number):
        autogui.press('tab')

def calibrate():
    variables = []
    weight = 5
    
    # create parameters to automate teh seleection of the dictionnaries
    
    webbrowser.open('https://www.japhy.fr/profile-builder/', new=1)
    time.sleep(2)
    popupmsg('calibration has started we will guide you')
    
    # number of animal variable

    popupmsg('hover the mouse on the option that says 1 animal, do not click !!!')
    time.sleep(2)
    print(autogui.size())
    autogui.click(autogui.position())
    variables.append(autogui.position)
    
    # type of animal variable

    popupmsg('hover over the dog')
    time.sleep(2)
    autogui.click(autogui.position())
    variables.append(autogui.position)
    time.sleep(1)
    autogui.write(get_name())
    autogui.press('enter')
    
    #sexe variables
    #female var

    popupmsg('hover over female')
    time.sleep(2)
    variables.append(autogui.position)
    
    #male varialbe

    popupmsg('hover over male')
    time.sleep(2)
    autogui.click(autogui.position())
    variables.append(autogui.position)

    #varialble castrer non

    popupmsg("hover over non")
    time.sleep(1.5)
    variables.append(autogui.position)

    #variable castrer oui

    popupmsg("hover over oui")
    time.sleep(1.5)
    autogui.click(autogui.position())
    variables.append(autogui.position)
    time.sleep(2)

    # variable textbox position for the race 
     
    popupmsg("hover over the text box")
    time.sleep(2)
    variables.append(autogui.position())
    autogui.click(autogui.position(), clicks=2)
    autogui.write('shiba inu')
    autogui.press('tab')
    autogui.press('down')
    autogui.press('enter')
    tab_presses(2)
    autogui.press('enter')
    time.sleep(1)

    # the position for the suivant button of the age section 
    # is not needed, we can access it with keyboard presses
    
    tab_presses(5)
    autogui.press('enter')
    time.sleep(2)

    # variable lazy 

    popupmsg("hover over lazy ... you know the drill by now")
    time.sleep(2)
    variables.append(autogui.position())
    temp = autogui.position()

    #variable normal activity level

    popupmsg("hover over normal activity level...")
    time.sleep(2)
    variables.append(autogui.position())

    #varialbe very active

    popupmsg("hover over the last option")
    time.sleep(2)
    variables.append(autogui.position())
    autogui.click(temp.x, temp.y)
    time.sleep(1)
    popupmsg("i promise its almost over, look at the progress bar")
    
    # varialbe slim
    
    popupmsg("hover over slim")
    time.sleep(2)
    variables.append(autogui.position())
    temp = autogui.position()
    
    #varialble average body
    
    popupmsg("hover over normal")
    time.sleep(2)
    variables.append(autogui.position())
    
    #varialbe fat

    popupmsg("hover over fat, we dont body shame over here")
    time.sleep(2)
    variables.append(autogui.position())
    autogui.click(temp.x, temp.y)
    time.sleep(1)

    # the position for the button suivant in the section
    # for the weight is not needed since we can acces it with keyboard 
    # presses

    tab_presses(2)
    autogui.write(str(weight))
    tab_presses(3)
    autogui.press('enter')

    # variable for dry food position

    popupmsg("hover over only dry foods")
    time.sleep(2)
    variables.append(autogui.position())
    autogui.click(autogui.position())

    # variable position test menu

    popupmsg("hover over test menu")
    time.sleep(2)
    autogui.click(autogui.position())
    variables.append(autogui.position())

    #variable position finaliser
    variables.append(autogui.position())
    time.sleep(2)
    autogui.click(autogui.position())
    # the two above variables have the same position

    popupmsg('hover over apres mon essai')
    time.sleep(2)
    variables.append(autogui.position())
    autogui.click(autogui.position())

    with open('file.pkl', 'wb') as file:
      
    # A new file will be created
        pickle.dump(variables, file)

    popupmsg('congratulations you have successfully configured the script \n at least i hope so')
    
    # if there is time : play a video of anime girl dancing


def navigate_site():

    # same steps as function calibrate but without the popup messages 
    # and we need to send the information collected to a data base 
    # we need to loop throught this function and get all the possible 
    # combinations for the different var of the site

    age = 3
    weight = 5

    # create parameters to automate teh seleection of the dictionnaries
    webbrowser.open('https://www.japhy.fr/profile-builder/', new=2)
    time.sleep(2)

    print(autogui.size())
    autogui.click(x = 500, y = 800)
    time.sleep(1)
    autogui.click(x=1197, y=717)
    time.sleep(1)
    autogui.write(get_name())
    autogui.press('enter')
    time.sleep(2)
    autogui.click(x=662, y=550)
    time.sleep(0.5)
    autogui.click(x=662, y=550)
    time.sleep(2)
    autogui.click(x=871, y=490, clicks=2)
    autogui.write('shiba inu')
    autogui.press('tab')
    autogui.press('down')
    autogui.press('enter')
    tab_presses(2)
    autogui.press('enter')
    time.sleep(1)
    tab_presses(3)
    autogui.write(str(age))
    tab_presses(2)
    autogui.press('enter')
    time.sleep(2)
    autogui.click(fitness_level['lazy']['x'], fitness_level['lazy']['y'])
    time.sleep(1)
    autogui.click(body_type['thin']['x'], body_type['thin']['y'])
    time.sleep(1)
    tab_presses(2)
    autogui.write(str(weight))
    tab_presses(3)
    autogui.press('enter')
    time.sleep(2)
    autogui.click(x=706, y=605)
    time.sleep(1)
    autogui.hotkey('ctrl','a')
    autogui.hotkey('ctrl', 'c')
    DOG_MENU = paper.paste()
    print(DOG_MENU)
    create_file(DOG_MENU)
    print(NAME)

http = urllib3.PoolManager()
r = http.request('GET', 'https://www.japhy.fr/sur-mesure/japhy-b')
r.status

def create_file(string):
    try:
        with open('C:/Users/carlo/python_project/menu.txt', 'w') as f:
            f.write(string)
    except FileNotFoundError:
        print("The directory does not exist")

#navigate_site()
calibrate()