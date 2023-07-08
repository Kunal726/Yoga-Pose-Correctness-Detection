from tkinter import *

from tkinter import ttk



root = Tk()

root.title('Shavasana')

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
my_canvas.create_text(5,40,text="""Shavasana""",fill="white", font=('Helvetica 25 bold'))
my_canvas.create_text(20,300,text="""
How to do the Savasana / Corpse Pose

1.) Lie flat on your back, preferably without any props or cushions.
Use small pillow below your neck if absolutely required. Close your eyes.

2.) Keep your legs comfortable apart and let your feet and knees relax completely, toes facing to the sides.

3.) Place your arms alongside, yet a little spread apart from your body. Leave your palms open, facing upward.

4.) Taking your attention to different body parts one by one, slowly relax your entire body.

5.) Begin with bringing your awareness to the right foot, move on to the right knee (as you complete one leg, 
move your attention on to the other leg), and so on, and slowly move upwards to your head, relaxing each part of the body.

6.) Keep breathing slowly, gently, deeply and allow your breath to relax you more and more. The incoming breath energizes
the body while the outgoing breath brings relaxation. Drop all sense of hurry or urgency or any need to attend to anything else.
Just be with the body and the breath. Surrender the whole body to the floor and let go. Make sure you don’t fall asleep!

7.) After some time, about 10-20minutes when you feel fully relaxed, keeping your eyes closed, slowly roll onto your right side.
Lie in that position for a minute or so. Then, taking the support of your right hand, gently sit up into a seated pose such as Sukhasana (Easy Pose).

8.) Keep your eyes closed and take a few deep breaths in and out as you gradually become aware of your environment and the body.
When you feel complete, slowly and gently open your eyes.
""",fill="white", font=('Helvetica 15 bold'))


root.mainloop()