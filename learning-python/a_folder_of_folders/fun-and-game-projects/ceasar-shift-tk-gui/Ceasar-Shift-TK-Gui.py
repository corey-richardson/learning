import tkinter as tk
from tkinter import ttk
from tkinter import *

# Initialise a window as "gui", with title "Cyrtography" and size "700x350"
gui = tk.Tk()
gui.geometry("700x350")
gui.title("Cryptography")

# Label
label = ttk.Label(text="Ceasar Cipher Shifter")
label.config(anchor=CENTER)
label.pack(fill=tk.X, padx=5, pady=5)

# Define a function taking in the user inputted string and shift value
# Shift each letter by var:shift and add it to string "coded"
# Output the coded message as a label on screen
def encode(user_in,shift):
    coded = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(user_in)):
        if user_in[i] in alphabet:
            value = alphabet.find(user_in[i])
            coded += str(alphabet[(value+int(shift))%26])
        else:
            coded += user_in[i]
    label = ttk.Label(text="Shifted %s: %s" % (shift,coded))
    label.config(anchor=CENTER)
    label.pack(fill=tk.X, padx=5, pady=5)
            
# Define a variable that will "get" the inputted value from the entry box
# Display this message on screen
# Pass the string into encode()    
def get_input():
    global shift
    user_in = entry.get()  
    label = ttk.Label(text="In: " + user_in)
    label.config(anchor=CENTER)
    label.pack(fill=tk.X, padx=5, pady=5)
    encode(user_in.lower(),shift)

# Initialise an entry box allowing the user to input their message    
entry = Entry(gui)
entry.pack()

# Initialise a combobox allowing the user to select the shift value, -25 --> 26
shift = tk.StringVar()
shift_select = ttk.Combobox(textvariable=shift)
shift_select["values"] = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,
                          20,21,22,23,24,25,26,-25,-24,-23,-22,-21,-20,-19,-18,
                          -17,-16,-15,-14,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,
                          -2,-1)
shift_select["state"] = "readonly"
shift_select.pack(fill=tk.X,padx=200,pady=5)

# Define a function and call it when the combobox is altered
# The function gets the selected value and sets it to var:shift
def cmb_shift_changed(event):
    global shift
    shift = shift_select.get()
shift_select.bind("<<ComboboxSelected>>",cmb_shift_changed)

# Button to "set" the input and shift value, this will then call "get_input()"
Button(gui,text="Set",command=get_input).pack()

# Close and destroy the window
Button(gui,text="Close",command=gui.destroy).pack()
gui.mainloop()
