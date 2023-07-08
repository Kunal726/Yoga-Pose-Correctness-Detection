from tkinter import *

from tkinter import ttk



root = Tk()

root.title('Vajrasana')

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
my_canvas.create_text(5,40,text="""Vajrasana""",fill="white", font=('Helvetica 25 bold'))
my_canvas.create_text(20,300,text="""Vajra’ means diamond-shaped or thunderbolt; ‘asana’ means posture or pose.
Vajrasana has been named 
after the shape it takes – a diamond or thunderbolt. 
This asana is pronounced as vahj-RAH-sah-na.
If there is one holistic pose that you can slip into easily, and still gain a variety of benefits, it is the Vajrasana, the Adamantine Pose.

1.) Sit with your legs stretched straight in front of you.

2.) Now, fold both the legs and sit in a kneeling position. Keep the hips on the heels; the toes should point out behind you, and your big
toes should touch each other at the back.

3.) If you are a beginner, you may want to keep a cushion under your feet for comfort to prevent ankle pain.

4.) You can also choose to keep a cushion or blanket above the feet and below the knees, in case of knee pain. Don’t forget to consult your
doctor in case of some special medical conditions.

5.) Sit comfortably on the pit formed by the parted heels.

6.) Keep your head, neck, and spine in a straight line. Place your palms on your thighs, facing upwards.

7.) If you are an advanced yoga practitioner, hold this pose for about 15 minutes, while taking long and deep breaths. Beginners may start
with about 30 seconds, according to their comfort level. 

8.) Exhale and relax. 

9.) Straighten your legs.""",fill="white", font=('Helvetica 15 bold'))

root.mainloop()