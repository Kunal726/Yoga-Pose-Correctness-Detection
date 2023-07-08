import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import sqlite3
from subprocess import call

root = tk.Tk()
root.configure(background="gray")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Main")

image2 =Image.open('A2.jpg')
image2 =image2.resize((670,880), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=950, y=0)

frame_alpr = tk.LabelFrame(root, text="  ", width=960, height=980, bd=0, font=('times', 14, ' bold '),bg="lightyellow")
frame_alpr.grid(row=0, column=0)
frame_alpr.place(x=0, y=0)

image2 =Image.open('S6.jpg')
image2 =image2.resize((140,120), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)
background_label = tk.Label(frame_alpr, image=background_image)

background_label.image = background_image

background_label.place(x=410, y=25)

lbl = tk.Label(frame_alpr, text="To Provide Correct Yoga pose detection &", font=('Times New Roman', 30,' bold '),bg="white",fg="black")
lbl.place(x=85, y=180)

lbl = tk.Label(frame_alpr, text="Real-time Pose Detection ", font=('Times New Roman', 30,' bold '),bg="white",fg="black")
lbl.place(x=200, y=250)

logo_label=tk.Label()
logo_label.place(x=90,y=55)


logo_label1=tk.Label(text='...To develop a system that is capable \n of detecting and identifying \n the Yoga poses...',compound='bottom',font=("Times New Roman", 20, 'bold', 'italic'),width=50, bg="white", fg="black")
logo_label1.place(x=120,y=650)


def login():
    call(["python", "GUI_main.py"])  
    
def window():
    root.destroy()

button1 = tk.Button(frame_alpr, text=" START",command=login,width=15, height=1, font=('times', 25, ' bold '),bg="brown",fg="black")
button1.place(x=350, y=450)

root.mainloop()