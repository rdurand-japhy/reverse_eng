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
NAME = ''
DOG_MENU = ''

fitness_level = {'lazy' : {'x': 486, 'y':637},
                 'normal' : {'x': 977, 'y' : 630},
                 'very active' :  {'x': 1427, 'y' : 630}}

body_type = {'thin' : {'x': 486, 'y':637},
             'normal' : {'x': 977, 'y' : 630},
              'fat' :  {'x': 1427, 'y' : 630}} #we dont body shame here


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
    webbrowser.open('https://www.japhy.fr/profile-builder/', new=2)
    time.sleep(2)
    popupmsg('calibration has started we will guide you')
    popupmsg('hover the mouse on the option that says 1 animal, do not click !!!')
    time.sleep(2)
    print(autogui.size())
    autogui.click(autogui.position())
    variables.append(autogui.position)
    popupmsg('hover over the dog')
    time.sleep(2)
    autogui.click(autogui.position())
    variables.append(autogui.position)
    time.sleep(1)
    autogui.write(get_name())
    autogui.press('enter')
    popupmsg('hover over male')
    time.sleep(2)
    autogui.click(autogui.position())
    variables.append(autogui.position)
    popupmsg("hover over oui")
    time.sleep(1.5)
    autogui.click(autogui.position())
    variables.append(autogui.position)
    time.sleep(2)
    tab_presses(2)
    autogui.write('shiba inu')
    autogui.press('tab')
    autogui.press('down')
    autogui.press('enter')
    tab_presses(2)
    autogui.press('enter')
    time.sleep(1)
    tab_presses(5)
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
    time.sleep(2)
    autogui.click(autogui.position())
    variables.append(autogui.position())
    variables.append(autogui.position())
    time.sleep(2)
    autogui.click(autogui.position())
    variables.append(autogui.position())
    with open('file.pkl', 'wb') as file:
      
    # A new file will be created
        pickle.dump(variables, file)

def navigate_site():
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
    tab_presses(5)
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