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
import cv2
import numpy as np

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


def navigate_site1():

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

def page_loaded(original : str):
    myScreenshot = autogui.screenshot()
    root_path  = os.getcwd()
    path = root_path + '\current_page.png'
    myScreenshot.save(path)


    if autogui.locateOnScreen('page_1.png', confidence=0.2) != None:
        return True
    else :
        return False



def navigate_site():
    popupmsg('VERY IMPORTANT TURN OFF DARK MODE ON YOUR CHROME, \n PERFORMANCE OF THE AI WILL BE AFFECTED IF DARK MODE IS TURNED ON!!!')
    sex  = ['male.png', 'femelle.png']
    castrer = ['castrer_oui.png', 'castrer_non.png']
    activity = ['actif_peu.png', 'actif_normale.png', 'actif_tres.png']
    fitness =  ['maigre.png', 'poids_normale.png','gros.png']
    for x in sex: 
        for y in castrer:
            for z in activity:
                for w in fitness:
                    for i in range(1, 10):
                        for n in range(8, 30):
                            webbrowser.open('https://www.japhy.fr/profile-builder/', new=2)
                            #page 1 is the page where we select the number of menus
                            while page_loaded('page_1.png') != True:
                                pass
                            posx, posy = find_position('current_page.png','1_animal.png')
                            print(posx, posy)

def find_position(screenshot :str, target : str):
        
    method = cv2.TM_SQDIFF_NORMED

    # Read the images from the file
    small_image = cv2.imread(target)
    large_image = cv2.imread(screenshot)

    result = cv2.matchTemplate(small_image, large_image, method)

    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    # Draw the rectangle:
    # Extract the coordinates of our best match

    MPx,MPy = mnLoc

    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = small_image.shape[:2]

    # Step 3: Draw the rectangle on large_image
    # the print statement shows the beginnig and end of the rectangle
    # print((MPx,MPy),(MPx+tcols,MPy+trows))
    
    # converting the coordinates of the square into the x, y coordinates of the mouse

    x = (MPx + MPx+tcols)/2
    y = (MPy + MPy+trows)/2

    return x,y

# the arguments target and screenshot are the string name of the icon image and the screenshot
# tested all possibilities every thing seems to work fine except male and female,
# the image recognition always picks femalle regardless of the input given
def icon_tester(screenshot : str, target : str):
    img1 = cv2.imread(target)
    img2 = cv2.imread(screenshot)
    
    orb = cv2.ORB_create()
    kp1 , des1 = orb.detectAndCompute(img1, None)
    kp2 , des2 = orb.detectAndCompute(img2, None)

    imgkp1 = cv2.drawKeypoints(img1, kp1, None)
    imgkp2 = cv2.drawKeypoints(img2, kp2, None)

    bf = cv2.BFMatcher()

    matches = bf.knnMatch(des1, des2, k=2)

    good = []
    for m, n in matches:
        if m.distance< 0.75*n.distance:
            good.append([m])


    img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags = 2)
    
    cv2.imshow('kp1', imgkp1)
    cv2.imshow('kp2', imgkp2)
    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)
    cv2.imshow('img3', img3)

    method = cv2.TM_SQDIFF_NORMED

    # Read the images from the file
    small_image = cv2.imread(target)
    large_image = cv2.imread(screenshot)

    result = cv2.matchTemplate(small_image, large_image, method)

    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    # Draw the rectangle:
    # Extract the coordinates of our best match
    MPx,MPy = mnLoc

    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = small_image.shape[:2]

    # Step 3: Draw the rectangle on large_image
    cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

    # Display the original image with the rectangle around the match.
    cv2.imshow('output',large_image)

    cv2.waitKey(0)
    

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


navigate_site()

#icon_tester('activiter.png', 'apres_essai_button.png')


#page_loaded('page_1.png')
#TODO add data retreiving for the content of the different menus ingredients etc