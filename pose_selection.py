import tkinter as tk
from subprocess import call
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
import imutils

global fn
fn = ""
##############################################
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Yoga Pose Correctness Detection")


# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('home.jpg')
image2 = image2.resize((1530, 1000), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="🧘  Yoga Pose Correctness Detection  🧘",font=("Helvetica", 40, 'bold'),
                    background="#000000", fg="white", width=50, height=2)
label_l1.place(x=0, y=0)


def action_sitting():
    call(["python", "yoga_sitting.py"])
    root.destroy()

def action_standing():
    call(["python", "yoga_stand.py"])
    root.destroy()



button3 = tk.Button(root, text="Standing Pose",command=action_standing, width=20, height=1,activebackground="#ffffff",activeforeground='#000000', bg="#000000", fg="white",font=('Helvetica', 20, 'bold'))
button3.place(x=100, y=220)

button3 = tk.Button(root, text="Sitting Pose",command=action_sitting, width=20, height=1,activebackground="#ffffff",activeforeground='#000000', bg="#000000", fg="white",font=('Helvetica', 20, 'bold'))
button3.place(x=100, y=320)

root.mainloop()