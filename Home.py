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

def help():
    frame_alpr = tk.LabelFrame(root, text=" --Yoga Poses-- ", width=900, height=550, bd=5, font=('times', 14, ' bold '),bg="SeaGreen1")
    frame_alpr.grid(row=0, column=0, sticky='nw')
    frame_alpr.place(x=450, y=120)

    image3 = Image.open('v.jpg')
    image3 = image3.resize((200, 200), Image.ANTIALIAS)
    background_image3 = ImageTk.PhotoImage(image3)
    background_label3 = tk.Label(root, image=background_image3,text="Vajrasan",compound='bottom')
    background_label3.image = background_image3
    background_label3.place(x=500, y=150)
    
    
    image4 = Image.open('s.jpg')
    image4 = image4.resize((200, 200), Image.ANTIALIAS)
    background_image4 = ImageTk.PhotoImage(image4)
    background_label4 = tk.Label(root, image=background_image4,text="Shavasan",compound='bottom')
    background_label4.image = background_image4
    background_label4.place(x=700, y=150)
    
    image5 = Image.open('g.jpg')
    image5 = image5.resize((200, 200), Image.ANTIALIAS)
    background_image5 = ImageTk.PhotoImage(image5)
    background_label5 = tk.Label(root, image=background_image5,text="Gomukhaasan",compound='bottom')
    background_label5.image = background_image5
    background_label5.place(x=900, y=150)

    image22 = Image.open('garud.jpg')
    image22 = image22.resize((200, 200), Image.ANTIALIAS)
    background_image22 = ImageTk.PhotoImage(image22)
    background_label22 = tk.Label(root, image=background_image22,text="Bhadraasan",compound='bottom')
    background_label22.image = background_image22
    background_label22.place(x=1100, y=150)
    
    image6 = Image.open('b.jpg')
    image6 = image6.resize((200, 200), Image.ANTIALIAS)
    background_image6 = ImageTk.PhotoImage(image6)
    background_label6 = tk.Label(root, image=background_image6,text="Bhadraasan",compound='bottom')
    background_label6.image = background_image6
    background_label6.place(x=500, y=400)

    image22 = Image.open('garud.jpg')
    image22 = image22.resize((200, 200), Image.ANTIALIAS)
    background_image22 = ImageTk.PhotoImage(image22)
    background_label22 = tk.Label(root, image=background_image22,text="Garudasan",compound='bottom')
    background_label22.image = background_image22
    background_label22.place(x=500, y=400)
    
    image7 = Image.open('d.jpg')
    image7 = image7.resize((200, 200), Image.ANTIALIAS)
    background_image7 = ImageTk.PhotoImage(image7)
    background_label7 = tk.Label(root, image=background_image7,text="Dhanurasan",compound='bottom')
    background_label7.image = background_image7
    background_label7.place(x=700, y=400)


    image9 = Image.open('vrk.jpg')
    image9 = image9.resize((200, 200), Image.ANTIALIAS)
    background_image9 = ImageTk.PhotoImage(image9)
    background_label9 = tk.Label(root, image=background_image9,text="Vrksasana",compound='bottom')
    background_label9.image = background_image9
    background_label9.place(x=900, y=400)

    image10 = Image.open('vir.jpg')
    image10 = image10.resize((200, 200), Image.ANTIALIAS)
    background_image10 = ImageTk.PhotoImage(image10)
    background_label10 = tk.Label(root, image=background_image10,text="Virbhadrasana I",compound='bottom')
    background_label10.image = background_image10
    background_label10.place(x=1100, y=400)

    

    

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def action():
    call(["python","pose_selection.py"])
    root.destroy()

def login():
    call(["python","login.py"])
    root.destroy()

def info():
    call(["python","info.py"])
#################################################################################################################
def window():
    root.destroy()



button3 = tk.Button(root, text="Recognize Yoga Pose",command=action, width=20, height=1,activebackground="#ffffff",activeforeground='#000000', bg="#000000", fg="white",font=('Helvetica', 20, 'bold'))
button3.place(x=100, y=220)

button3 = tk.Button(root, text="Help",command=help, width=20, height=1,activebackground="#ffffff",activeforeground='#000000', bg="#000000", fg="white",font=('Helvetica', 20, 'bold'))
button3.place(x=100, y=320)

button3 = tk.Button(root, text="Log Out",command=login, width=20, height=1,activebackground="#ffffff",activeforeground='#000000', bg="#000000", fg="white",font=('Helvetica', 20, 'bold'))
button3.place(x=100, y=420)

button4 = tk.Button(root, text="Information",command=info, width=20, height=1,activebackground="#ffffff",activeforeground='#000000', bg="#000000", fg="white",font=('Helvetica', 20, 'bold'))
button4.place(x=100, y=520)

exit = tk.Button(root, text="Exit", command=window, width=14, height=1, font=('Helvetica', 20, 'bold'), bg="#000000",fg="white")
exit.place(x=140, y=620)


root.mainloop()