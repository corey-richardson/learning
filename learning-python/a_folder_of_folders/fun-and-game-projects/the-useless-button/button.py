import tkinter as tk
from tkinter import ttk
from tkinter import *

# read number from txt
# save to variable
# button increments variable by one
# display var as label
# when click on close button, save variable to file

# Opens the txt file and reads the number on the first line
# Sets this to the variable "counter"
with open("count.txt","r") as count_file:
    counter = count_file.readline()
counter=int(counter)

# Initialises a gui of size 100x50
gui = tk.Tk()
gui.geometry("100x50")

# Define a function that is called when the button is clicked
# This function will increment the counter by 1, update the button text 
# and write the new counter value to the txt
def on_click():
    # Access and increment counter by 1
    global counter
    counter+=1
    # Update the button text to the new counter value
    btn_text.set(counter)
    # Open the txt in write mode and write the new counter variable
    with open("count.txt","w") as count_file:
        count_file.write(str(counter))
        
# Initialises a button with text matching the current count value and with
# the command to run func:on_click when it is interacted with.
btn_text = tk.StringVar()
btn_text.set(counter)
button = ttk.Button(gui,textvariable=btn_text,command=on_click).pack()

# tkinter 
gui.mainloop()