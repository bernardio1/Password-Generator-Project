# Strong password Generator
# Importing the tkinter module
import random
from tkinter import *

# importing the pyperclip module to use it to copy our generated password to clipboard

import pyperclip

# initializing tkinter
root = Tk()
# setting the width and height of the gui
root.geometry("700x500")  # x is small case here

# declaring a variable of integer type which will be used to
# store the length of the password generated
passstr = StringVar()
# stroing the length of the password entered by the user
passlen = IntVar()

# setting the length of the password to zero initially
passlen.set(0)


# function to generate password

def generate():
    # storing the key in a list that will be used to generate the password
    pass1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
             "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
             "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8",
             "9", "0", "!", "@", "#", "$", "%", "^", "&", "*"]

    # declaring password to be empty
    password = ""

    # loop to generate the random password of the length
    for x in range(passlen.get()):
        password = password + random.choice(pass1)

    # setting password to entry widget
    passstr.set(password)


def copytoclipboard():
    random_password = passstr.get()


# creating a text label widget
Label(root, text="Password Generator Application", font="calibre 20 bold").pack()
# creating a text label widget
Label(root, text=" Enter your password length").pack(pady=3)
# creating an entry widget to take password length entered by the user
Entry(root, textvariable=passlen).pack(pady=3)
# button to call the generated password
Button(root, text="Generate Password ", command=generate, highlightcolor="GREEN").pack(pady=7)
# entry widget to show password generated
Entry(root,textvariable=passstr).pack(pady=3)
#button to call the clipboard function
Button(root, text="Copy to Clipboard", command = copytoclipboard).pack()

#mainloop() is an infinite loop uset o run the application when it is in ready state
root.mainloop()
