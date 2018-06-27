# My second python project, a project manager to keep manage of all my projects and with ease create new ones



# Imports
import os
import sys
#import fileManagement
# Imports


# Variables
intro = """  
  _____           _           _     __  __                                                  
 |  __ \         (_)         | |   |  \/  |                                                 
 | |__) | __ ___  _  ___  ___| |_  | \  / | __ _ _ __   __ _  __ _  ___ _ __                
 |  ___/ '__/ _ \| |/ _ \/ __| __| | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|               
 | |   | | | (_) | |  __/ (__| |_  | |  | | (_| | | | | (_| | (_| |  __/ |                  
 |_|   |_|  \___/| |\___|\___|\__| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|                  
  _             _/ |                          _     ______    __/ |                         
 | |           |__//\                        | |   |  ____|  |___/                          
 | |__  _   _     /  \  _   _  __ _ _   _ ___| |_  | |__  _   _ _ __ ___   __ _ _ __  _ __  
 | '_ \| | | |   / /\ \| | | |/ _` | | | / __| __| |  __|| | | | '_ ` _ \ / _` | '_ \| '_ \ 
 | |_) | |_| |  / ____ \ |_| | (_| | |_| \__ \ |_  | |___| |_| | | | | | | (_| | | | | | | |
 |_.__/ \__, | /_/    \_\__,_|\__, |\__,_|___/\__| |______\__, |_| |_| |_|\__,_|_| |_|_| |_|
         __/ |                 __/ |                       __/ |                            
        |___/                 |___/                       |___/                          
Welcome to project manager by August Eymann\n

This was created so I can easily manage my python projects, create new ones and learn some new things at the same time.

Type in info for more options
"""
infopage = "Options:\nNew: Creates a new folder with a main.py file\nRemove: Delete's a project\nInfo: Provides Information about the manager"
options = ["new","remove","info"]
proceed = False
# Variables

print(intro)
while proceed == False:
    starting = input("What would you like to do?\n")
    if (not starting.lower()) in options:
        print("Not a valid command try again")
    elif (starting.lower()) == "info":
        print(infopage)
    ending = input("Would you like to quit\n")
    if ("y" in ending.lower()):
        sys.exit("Project Manager exited")    