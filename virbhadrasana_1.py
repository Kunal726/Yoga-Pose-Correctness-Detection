from tkinter import *

from tkinter import ttk



root = Tk()

root.title('Virbhadrasana I')

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


my_canvas.create_text(0,0,text="""Asana's Information""",fill="white", font=('Helvetica 25 bold'))
my_canvas.create_text(5,40,text="""Virbhadrasana I""",fill="white", font=('Helvetica 25 bold'))
my_canvas.create_text(20,300,text="""Virabhadrasana is also known as the warrior pose. The term Virabhadrasana is composed of three words:
Vira which means courageous, warrior or vigorous; Badra means auspicious or good, while asana refers to posture.
Warrior pose is a standing yoga that provides strength to the shoulders, arms, thighs, and muscles of the back

The steps to practice Virabhadrasana I are: 

1.) Take a Tadasana pose (Mountain pose). Separate the legs from a distance of at least 3 to 4 feet with one exhalation. 
2.) Raise your arms parallel to the ground and perpendicular to one another. Draw the scapulae toward the hip bone by
pressing firmly into the back. 
3.) Rotate your right foot 90 degrees to the right while rotating your left foot 45 to 60 degrees to the right.  
4.) Right, and left heels should be in line. Exhale as you rotate your torso to the right, trying to keep the front edge
of the mat as close to your pelvis as you can. 
5.) Exhale, bending the right knee above the right ankle to bring the body into a perpendicular position with the floor. 
6.) Lift the ribs away from the pelvis with a forceful reach from the pelvis.
You will experience a lift in the back leg, chest, belly, and arms when you land on your back foot. 
7.) Bring the palms together if you can. Reach up a little via the pinky sides of the hands with the palms spread apart. 
8.) Stay there for 30 to 60 seconds. Exhaling, straighten the right knee while reaching the arms and pressing the back
heel firmly into the floor to stand up. 
9.) While breathing, rotate the legs forward and relax the arms, or keep them raised for a harder task. 
10.) After taking a few deep breaths, bend your legs to the left and repeat for the same amount of time.
11.) Return to Tadasana after completing this asana. """,fill="white", font=('Helvetica 14 bold'))

root.mainloop()