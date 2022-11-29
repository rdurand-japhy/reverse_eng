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
from PIL import Image, ImageTk
from itertools import count
import os 
from selenium import webdriver
from calibration import *
from pathlib import Path

FILE_NAME = ''
DOG_MENU = ''


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

def load(variable):
    #load variables from the calibration.pkl file to the calibration.py file
    iter = 0
    file =  open('calibration.pkl', 'rb')
    var = pickle.load(file)
    file.close()  
    print("the values loaded : \n",var)
    for x in variable:
        variable[x] = var[iter]
        iter += 1
        print(x,variable[x])
    file.close()
    

def calibrate():
    var = []
    weight = 5
    #checking if the calibration.pkl file exists
    #if yes the calibration is skipped 
    path = os.path.dirname(os.path.abspath("calibration.py"))
    path  += '/calibration.pkl'
    if not os.path.exists(path):
        popupmsg("please make sure that you have chrome installed before starting the calibration")
        # create parameters to automate teh seleection of the dictionnaries
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.japhy.fr/profile-builder/")
        time.sleep(2)
        popupmsg('calibration has started we will guide you')
        
        # number of animal variable

        popupmsg('hover the mouse on the option that says 1 animal, do not click !!!')
        time.sleep(2)
        print(autogui.size())
        autogui.click(autogui.position())
        var.append((autogui.position()[0], autogui.position()[1]))
        
        # type of animal variable

        popupmsg('hover over the dog')
        time.sleep(2)
        autogui.click(autogui.position())
        var.append((autogui.position()[0], autogui.position()[1]))
        time.sleep(1)
        autogui.write(get_name())
        autogui.press('enter')
        
        #sexe variables
        #female var

        popupmsg('hover over female')
        time.sleep(2)
        var.append((autogui.position()[0], autogui.position()[1]))
        
        #male varialbe

        popupmsg('hover over male')
        time.sleep(2)
        autogui.click(autogui.position())
        var.append((autogui.position()[0], autogui.position()[1]))

        #varialble castrer non

        popupmsg("hover over non")
        time.sleep(1.5)
        var.append((autogui.position()[0], autogui.position()[1]))

        #variable castrer oui

        popupmsg("hover over oui")
        time.sleep(1.5)
        autogui.click(autogui.position())
        var.append((autogui.position()[0], autogui.position()[1]))
        time.sleep(2)

        # variable textbox position for the race 
        
        popupmsg("hover over the text box")
        time.sleep(2)
        var.append((autogui.position()[0], autogui.position()[1]))
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
        var.append((autogui.position()[0], autogui.position()[1]))
        temp = autogui.position()

        #variable normal activity level

        popupmsg("hover over normal activity level...")
        time.sleep(2)
        var.append((autogui.position()[0], autogui.position()[1]))

        #varialbe very active

        popupmsg("hover over the last option")
        time.sleep(2)
        var.append((autogui.position()[0], autogui.position()[1]))
        autogui.click(temp.x, temp.y)
        time.sleep(1)
        popupmsg("i promise its almost over, look at the progress bar")
        
        # varialbe slim
        
        popupmsg("hover over slim")
        time.sleep(2)
        var.append((autogui.position()[0], autogui.position()[1]))
        temp = autogui.position()
        
        #varialble average body
        
        popupmsg("hover over normal")
        time.sleep(2)
        var.append((autogui.position()[0], autogui.position()[1]))
        
        #varialbe fat

        popupmsg("hover over fat, we dont body shame over here")
        time.sleep(2)
        var.append((autogui.position()[0], autogui.position()[1]))
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
        var.append((autogui.position()[0], autogui.position()[1]))
        autogui.click(autogui.position())

        # variable position test menu

        popupmsg("hover over test menu")
        time.sleep(2)
        autogui.click(autogui.position())
        var.append((autogui.position()[0], autogui.position()[1]))

        #variable position finaliser
        var.append((autogui.position()[0], autogui.position()[1]))
        time.sleep(2)
        autogui.click(autogui.position())
        # the two above variables have the same position

        popupmsg('hover over apres mon essai')
        time.sleep(2)
        var.append((autogui.position()[0], autogui.position()[1]))
        autogui.click(autogui.position())

        with open('calibration.pkl', 'wb') as file:
        
        # A new file will be created
            pickle.dump(var, file)

        popupmsg('congratulations you have successfully configured the script \n at least i hope so')
        
        # if there is time : play a video of anime girl dancing
        #===========================================================#        
        
        #                       anime girl dancing
        anime_girl()

        #===========================================================#
    else :
        #load the variables in the array and then in the correct variable names
        #start the site navigate function
        load(variables)
        navigate_site()
        pass


def navigate_site():

    # same steps as function calibrate but without the popup messages 
    # and we need to send the information collected to a data base 
    # we need to loop throught this function and get all the possible 
    # combinations for the different var of the site
    # elements to iterate throught
    # sex, castrer, race, activity level, fitness level
    #5 for loops we will omit looping through the breeds for now 
    # will be added in a later version 
    sex = [variables["sexe_male_position"],variables["sexe_female_position"] ]
    castrer = [variables["castrer_oui_position"],variables["castrer_non_position"] ]
    activity = [variables["position_peu_actif"],variables["position_moyen_actif"], variables["position_tres_actif"]]
    fitness = [variables["position_peu_maigre"],variables["position_ideal_corps"], variables["position_gros_coprs"]]

    for x in sex: 
        for y in castrer:
            for z in activity:
                for w in fitness:
                    for i in range(1, 10):
                        for n in range(8, 30):
                # create parameters to automate teh seleection of the dictionnaries
                            webbrowser.open('https://www.japhy.fr/profile-builder/', new=2)
                            time.sleep(3)

                            print(autogui.size())
                            autogui.click(variables["number_of_animals"])
                            time.sleep(1)
                            autogui.click(variables["dog_position"])
                            time.sleep(1)
                            autogui.write(get_name())
                            autogui.press('enter')
                            time.sleep(2)
                            # iterate between male and female
                            autogui.click(x)
                            time.sleep(0.5)
                            #castrer
                            autogui.click(y)
                            time.sleep(2)
                            autogui.click(variables["position_race_text_box"])
                            autogui.write('shiba inu')
                            autogui.press('tab')
                            autogui.press('down')
                            autogui.press('enter')
                            tab_presses(2)
                            autogui.press('enter')
                            time.sleep(1)
                            tab_presses(2)
                            autogui.write(str(i))
                            tab_presses(3)
                            autogui.press('enter')
                            time.sleep(2)
                            autogui.click(z)
                            time.sleep(1)
                            autogui.click(w)
                            time.sleep(1)
                            tab_presses(2)
                            autogui.write(str(n))
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

                        http = urllib3.PoolManager()
                        r = http.request('GET', 'https://www.japhy.fr/sur-mesure/japhy-b')
                        r.status

# open line is prone to errors if we run the script on a other system 
def create_file(string):
    p = Path(__file__).with_name('menu.txt')
    try:
        with p.open('w',encoding="utf-8") as f:
            f.write(string)
    except FileNotFoundError:
        print("The directory does not exist")

#navigate_site()
#calibrate()

class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

def anime_girl():
    root = tk.Tk()
    root.title("finished !!")
    root.geometry("500x500")
    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('2eSh.gif')
    root.mainloop()

def test():
    number_of_animals = variables[0]
    time.sleep(2)
    number_of_animals = (autogui.position()[0], autogui.position()[1])
    print(number_of_animals)


calibrate()

#TODO add data retreiving for the content of the different menus ingredients etc