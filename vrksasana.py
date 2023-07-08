from tkinter import *

from tkinter import ttk



root = Tk()

root.title('Vrksasana')

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

my_canvas.create_text(0,0,text="""Asana's Information""",fill="white", font=('Helvetica 25 bold'))
my_canvas.create_text(5,40,text="""Vrksasana""",fill="white", font=('Helvetica 25 bold'))
my_canvas.create_text(20,360,text="""Vrksasana (Tree Pose) teaches you to simultaneously press down and feel rooted as you reach tall like
the branches of a mighty tree. In this pose, you find a sense of groundedness through the strength of your standing leg. Bringing the sole
of your opposite foot to your shin or thigh challenges your balance.

How to do Tree Pose

1.) Stand in Tadasana. Spread your toes, press your feet into the mat and firm your leg muscles. Raise your front hip points toward your
lower ribs to gently lift in your lower belly.

2.) Inhale deeply, lifting your chest, and exhale as you draw your shoulder blades down your back. Look straight ahead at a steady gazing spot.

3.) Place your hands on your hips and raise your right foot high onto your left thigh or shin. Avoid making contact with the knee.

4.) Press your right foot and left leg into each other.

5.) Check that your pelvis is level and squared to the front.

6.) When you feel steady, place your hands into Anjali Mudra at the heart or stretch your arms overhead like branches reaching into the sun.

7.) Hold for several breaths, then step back into Mountain Pose and repeat on the other side.

8.) Uncross your legs and repeat for the other leg.""",fill="white", font=('Helvetica 15 bold'))

root.mainloop()