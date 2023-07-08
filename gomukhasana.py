from tkinter import *

from tkinter import ttk



root = Tk()

root.title('Gomukhasana')

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
my_canvas.create_text(5,40,text="""Gomukhasana""",fill="white", font=('Helvetica 25 bold'))
my_canvas.create_text(20,300,text="""A Sanskrit word, Gomukhasana literally translates into a cow face posture 
(go – cow, mukha – face, asana – pose). A seated yoga posture, Gomukhasana can be performed along with a set of different seated asanas.
It helps stretch the arms, triceps, shoulders, and chest. Requiring the practitioner to sit erectly, it also enhances one’s posture.

How to do Gomukhasana

1. Sit on the yoga mat with your back straight and legs extended in front of you. Put your feet together and place your palms next to your hips.

2. Bend your right leg and place the right feet under your left buttock.

3. Stack your left knee over your right knee.

4. Raise the left arm above your head and bend the elbow. Simultaneously, bring the right arm behind your back and interlock both hands.

5. Take deep ujjayi breaths and stay as long as you are comfortable.

6. Now, as you exhale, release your arms.

7. Uncross your legs and repeat for the other leg.""",fill="white", font=('Helvetica 15 bold'))

root.mainloop()