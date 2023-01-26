# file renamer

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import *
import os
from os import listdir

directory= fd.askdirectory()

print(directory)
files = [file for file in listdir(directory)]

for file in files:
    try:
        old_dir = directory+"/"+file
        new_dir = file.lower()
        new_dir = file.replace(" ","-")
        new_dir = new_dir.replace("_","-")
        new_dir = directory + "/" +new_dir
        
        os.rename(old_dir, new_dir)
        
        print(old_dir)
        print("-->")
        print(new_dir)
        print("")
    except FileExistsError:
        pass