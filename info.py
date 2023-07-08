from tkinter import *

from tkinter import ttk
from subprocess import call




root = Tk()

root.title('INFORMATION')

root.geometry("1920x1080")



# Create A Main frame

main_frame = Frame(root)

main_frame.pack(fill=BOTH,expand=1)



# Create Frame for X Scrollbar

sec = Frame(main_frame)

sec.pack(fill=X,side=BOTTOM)



# Create A Canvas

my_canvas = Canvas(main_frame, bg='black')

my_canvas.pack(side=LEFT,fill=BOTH,expand=1)



# Add A Scrollbars to Canvas

x_scrollbar = ttk.Scrollbar(sec,orient=HORIZONTAL,command=my_canvas.xview)

x_scrollbar.pack(side=BOTTOM,fill=X)

y_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
y_scrollbar.pack(side=RIGHT,fill=Y)



# Configure the canvas

my_canvas.configure(xscrollcommand=x_scrollbar.set)

my_canvas.configure(yscrollcommand=y_scrollbar.set)

my_canvas.bind("<Configure>",lambda e: my_canvas.config(scrollregion= my_canvas.bbox(ALL))) 



#Create Another Frame INSIDE the Canvas

second_frame = Frame(my_canvas)



# Add that New Frame a Window In The Canvas

my_canvas.create_window((0,0),window= second_frame, anchor="nw")

def bhadrasana():
	call(["python","bhadrasana.py"])

def Vajrasana():
	call(["python","vajrasana.py"])

def Dhanurasana():
	call(["python","dhanurasana.py"])

def Shavasana():
	call(["python","shavasana.py"])

def Gomukhasana():
	call(["python","gomukhasana.py"])

def Vrksasana():
	call(["python","vrksasana.py"])

def Virbhadrasana_I():
	call(["python","virbhadrasana_1.py"])

my_canvas.create_text(0,0,text="""Project Information""",fill="white", font=('Helvetica 35 bold'))
my_canvas.create_text(5,100,text="""This Project aims to develop a robust system which is able to detect human poses 
and that too "Yoga Poses" to be specific. It uses Classification Algorithm called Logistic Regression 
to classify among various different Yoga Poses and that too with an great accuracy.""",fill="white", font=('Helvetica 20 bold'))

my_canvas.create_text(5,200,text="""Click on Asana for Information !""",fill="white", font=('Helvetica 30 bold'))

btn1 = Button(my_canvas, text="Bhadrasana", command = bhadrasana,width=15,height=3,bg='black',fg='white',font=('Helvetica', 10, 'bold'))
btn1.place(x=5, y=300)

btn1 = Button(my_canvas, text="Vajrasana", command = Vajrasana,width=15,height=3,bg='black',fg='white',font=('Helvetica', 10,'bold'))
btn1.place(x=140, y=300)
btn1 = Button(my_canvas, text="Dhanurasana", command = Dhanurasana,width=15,height=3,bg='black',fg='white',font=('Helvetica', 10, 'bold'))
btn1.place(x=275, y=300)

btn1 = Button(my_canvas, text="Shavasana", command = Shavasana,width=15,height=3,bg='black',fg='white',font=('Helvetica', 10, 'bold'))
btn1.place(x=410, y=300)

btn1 = Button(my_canvas, text="Gomukhasana", command = Gomukhasana,width=15,height=3,bg='black',fg='white',font=('Helvetica', 10, 'bold'))
btn1.place(x=545, y=300)

btn1 = Button(my_canvas, text="Vrksasana", command = Vrksasana,width=15,height=3,bg='black',fg='white',font=('Helvetica', 10, 'bold'))
btn1.place(x=680, y=300)

btn1 = Button(my_canvas, text="Virbhadrasana I", command = Virbhadrasana_I,width=15,height=3,bg='black',fg='white',font=('Helvetica', 10, 'bold'))
btn1.place(x=815, y=300)

btn1 = Button(my_canvas, text="Utkasana", command = Virbhadrasana_I,width=15,height=3,bg='black',fg='white',font=('Helvetica', 10, 'bold'))
btn1.place(x=5, y=380)

btn1 = Button(my_canvas, text="Navasana", command = Virbhadrasana_I,width=15,height=3,bg='black',fg='white',font=('Helvetica', 10, 'bold'))
btn1.place(x=140, y=380)

btn1 = Button(my_canvas, text="Prasarita", command = Virbhadrasana_I,width=15,height=3,bg='black',fg='white',font=('Helvetica', 10, 'bold'))
btn1.place(x=275, y=380)

btn1 = Button(my_canvas, text="Garudasana", command = Virbhadrasana_I,width=15,height=3,bg='black',fg='white',font=('Helvetica', 10, 'bold'))
btn1.place(x=410, y=380)

btn1 = Button(my_canvas, text="Trikonasana", command = Virbhadrasana_I,width=15,height=3,bg='black',fg='white',font=('Helvetica', 10, 'bold'))
btn1.place(x=545, y=380)

root.mainloop()