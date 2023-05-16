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
from pathlib import Path
import cv2
import numpy as np
import win32clipboard
import exel


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

def screenshot():
    image = autogui.screenshot()
    image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
    cv2.imwrite("screenshot.png", image)

def click(target):
    screenshot()
    position = find_position("screenshot.png",target)
    autogui.click(position)
    time.sleep(1)

def navigate_site():
    sex  = ['male.png', 'femelle.png']
    castrer = ['castrer_oui.png', 'castrer_non.png']
    activity = ['actif_peu.png', 'actif_normale.png', 'actif_tres.png']
    fitness =  ['maigre.png', 'poids_normale.png','gros.png']

    for x in sex: 
        for y in castrer:
            for z in activity:
                for w in fitness:
                    for i in range(1, 10): # age
                        for n in range(8, 30): # weight
                                get_to_starting_position()
                                time.sleep(2)
                                click(x)
                                
                                # castrer or not
                                castrer_or_not(y)
                                
                                # chose the race of the dog
                                enter_race('shiba inu')
                                
                                # enter age
                                enter_age(i)
                                
                                click(z)
                                
                                click(w)

                                # enter weight
                                enter_weight(n)

                                # select croquette type

                                click('croquettes.png')

                                # get html
                                get_html()

                                # get html indices
                                indicies =search_string_text_file('libs-ui-src-ProductCard__title--LgNam')

                                # get the meals
                                meals  = menu_items(indicies)
                                
                                # proceed in the site
                                click('proceed_menu.png')

                                # proceed to the finalized order
                                click('finaliser_commande_button.png')
                                
                                # proceed to the payment
                                click('apres_essai_button.png')


                                get_html()

                                # find the price of the menu
                                # only the first price is taken
                                indicies =search_string_text_file('libs-ui-src-ProductCard__title--LgNam')

                                price = menu_price(indicies[0])

                                price = seperating_integer_from_string(price)

                                # removing the .png from the strings
                                sex_str = x[:-4]
                                castrer_str = y[:-4]
                                activity_str = z[:-4]
                                fitness_str = w[:-4]

                                # send the information to the exel file
                                # put all the values in a single array
                                array = [sex_str, castrer_str,'shiba inu',i, activity_str, fitness_str, n, meals[0], meals[1], price]
                                exel.add_data(array)
    anime_girl()

def castrer_or_not(decision):
    if decision == 'castrer_oui.png':
        tab_presses(1)
        autogui.press('enter')
        time.sleep(1)
    else:
        tab_presses(2)
        autogui.press('enter')
        time.sleep(1)
                                
def search_string_text_file(search_string):
    indices = []
    #search the string in the text file
    #open the file
    p = Path(__file__).with_name('menu.txt')
    #read the file
    #search the string
    #return the position of the string
    with open(p, 'r') as file:

        for line_number, line in enumerate(file, 1):
                start_index = line.find(search_string)
                while start_index >= 0:
                    indices.append((line_number, start_index))
                    start_index = line.find(search_string, start_index + len(search_string))
        return indices

def seperating_integer_from_string(string):
    int_string = ""
    for char in string:
        if char.isdigit():
            int_string += char
        if char == ",":
            int_string += ","
    return int_string

def menu_price(index):
    #open the file
    p = Path(__file__).with_name('menu.txt')

    # open the sample file used
    file = open(p, 'r')
    
    # read the content of the file opened
    content = file.readlines()
    
    # read 10th line from the file
    print(content[index])
    return (content[index])

def menu_items(indicies):
    #open the file
    p = Path(__file__).with_name('menu.txt')

    # open the sample file used
    file = open(p, 'r')
    
    # read the content of the file opened
    content = file.readlines()
    
    # read 10th line from the file
    
    print(content[indicies[0][0] + 1])
    print(content[indicies[1][0] + 1])

    return (content[indicies[0][0] + 1],  content[indicies[1][0] + 1])

def get_html():
    autogui.click(button='right')
    autogui.press('up')
    autogui.press('enter')
    time.sleep(2)
    autogui.press('up', 50)
    autogui.press('down')
    time.sleep(4)
    autogui.hotkey('ctrl', 'c')
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    create_file(data)

def enter_weight(weight):
    tab_presses(2)
    weight = weight/2.2
    weight = round(weight, 1)
    autogui.write(str(weight))
    tab_presses(3)
    autogui.press('enter')
    time.sleep(1)

def get_to_starting_position():
    #we first need to navigate to the part where it asks if it is a male or a female
    #---------------------------------------------------------------------------------
    #we open the webpage and wait for it too load
    webbrowser.open('https://www.japhy.fr/profile-builder/', new=2)
    time.sleep(3)
    
    #scan the page for the image that indicates 1 animal and click on it
    click('1_animal.png')
    #---------------------------------------------------------------------------------
    # do the same steps for the dog selection
    time.sleep(1)
    click('chien.png')
    #enter name of pet
    time.sleep(1)
    autogui.write(get_name())
    autogui.press('enter')
    #---------------------------------------------------------------------------------

def enter_age(age):
    tab_presses(2)
    autogui.write(str(age))
    tab_presses(3)
    autogui.press('enter')
    time.sleep(1)

def enter_race(race):
    tab_presses(1)
    autogui.write(race)
    autogui.press('tab')
    autogui.press('down')
    autogui.press('enter')
    tab_presses(2)
    autogui.press('enter')
    time.sleep(1)

def find_position(screenshot, target):
    target = Path(__file__).resolve().with_name('pictures').joinpath(target)
    target = str(target)
    img1 = cv2.imread(target,0)
    img2 = cv2.imread(screenshot,0)
    
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

    #this shows the detection here for debugging purposes 

    # cv2.imshow('kp1', imgkp1)
    # cv2.imshow('kp2', imgkp2)
    # cv2.imshow('img1', img1)
    # cv2.imshow('img2', img2)
    # cv2.imshow('img3', img3)

        
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
    #converting the begennig and end positions to be the center of the rectangle only
    return (MPx + (tcols/2),MPy +(trows/2))

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


# TODO add data retreiving for the content of the different menus ingredients etc
# TODO add a function to get the information about the ingredients of the menu and the size of the croquettes
# TODO get the final price of croquettes
# TODO put all the reference pictures in a seperate file and change the path to the pictures to the pictures in the file