from tkinter import *

from tkinter import ttk



root = Tk()

root.title('Bhadrasana')

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
my_canvas.create_text(5,40,text="""Bhadrasana""",fill="white", font=('Helvetica 25 bold'))
my_canvas.create_text(10,300,text="""@Ancient India Yoga texts such as the Hatha Yoga Pradipika as well as the Gheranda Samhita mention this asana.
@ Yogi Swatmarama describes it as one of the 4 main Asanas that can be done for prolonged meditation.
@ Bhadrasana is considered as the 4th Asana appropriate for extended periods of sitting. It says that a yogi can get rid of fatigue by sitting
in this Asana.

Starting position:
1.) Sit on the mat. The legs fully stretched forward, toes together– pointing upwards. Keep the hands beside the body, palms resting on mat.
2.) Keep the neck straight and the upper body (chest) forward.  
3.) The stomach held in normal contour. And keep the chin drawn in. Focus eyes at one point straight ahead.

The sequence of steps to perform Yogendra Bhadrasana or the throne posture:
1.) Inhaling, in 3 seconds, draw both the legs close to the body. Now, keeping the legs in contact with the floor, with the knees bent outward
and the soles of the feet together.
2.) Bring the feet, with the toes pointing outward, close to the generative organ, the heels touching the perineum very closely. If required, 
clasp the feet to bring the heels as close to the body as possible.
3.) Once this position is secured, place the hands on the respective knees pressing them down. Keep the upper part of the body and the neck erect.  
4.) Maintain this position for 6 seconds, retaining the breath (final position).
5.) Return to starting position: Exhaling, in 3 seconds, return to the starting position, by slowly stretching the legs.""",fill="white", font=('Helvetica 15 bold'))

root.mainloop()