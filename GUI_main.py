import tkinter as tk
from tkinter import ttk, LEFT, END
from subprocess import call
from PIL import Image, ImageTk
from tkinter import messagebox as ms
import cv2
import sqlite3
import numpy as np
##############################################+=============================================================
root = tk.Tk()
root.configure(background="white")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("YOGA POSE CORRECTNESS DETECTION")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('home.jpg')
#image2 = image2.resize((960,850), Image.ANTIALIAS)
image2 = image2.resize((1800,1080), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)

label_l1 = tk.Label(root, text="🧘  Yoga Pose Correctness Detection  🧘",font=("Helvetica", 40, 'bold'),
                    background="#000000", fg="white", width=50, height=2)
label_l1.place(x=0, y=0)


def reg():
    call(["python","registration.py"])
    root.destroy()

def log():
    call(["python","login.py"])
    root.destroy()
    
def window():
  root.destroy()


button1 = tk.Button(root, text="Log In",command=log, width=20, height=1,activebackground="#ffffff",activeforeground='#000000', bg="#000000", fg="white",font=('Helvetica', 20, 'bold'))
button1.place(x=565, y=330)

button2 = tk.Button(root, text="Register",command=reg, width=20, height=1,activebackground="#ffffff",activeforeground='#000000', bg="#000000", fg="white",font=('Helvetica', 20, 'bold'))
button2.place(x=565, y=410)

button3 = tk.Button(root, text="Exit",command=window, width=20, height=1,activebackground="#ffffff",activeforeground='#000000', bg="#000000", fg="white",font=('Helvetica', 20, 'bold'))
button3.place(x=565, y=490)

root.mainloop()