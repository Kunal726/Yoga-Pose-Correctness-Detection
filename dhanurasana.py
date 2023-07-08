from tkinter import *

from tkinter import ttk



root = Tk()

root.title('Dhanurasana')

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
my_canvas.create_text(5,40,text="""Dhanurasana""",fill="white", font=('Helvetica 25 bold'))
my_canvas.create_text(20,300,text="""The bow has frequently been referenced in Indian mythology. In the Ramayana, Lord Rama broke Lord Shiva’s
bow at princess Sita’s swayamvara to win her hand in marriage, a feat that no other prince could do, indicating his divinity. In the Mahabharata,
some of the greatest duels involved the bow and arrow. Both prince Arujuna and his arch enemy Karna were adept at using the bow and arrow.
However, Arjuna surpassed all others in archery with his determination and constant practice. It is this determination and consistency that you
will explore within yourself as you smoothly move into Dhanurasana.

How to do Dhanurasana (Bow Pose)

1.) Lie on your stomach with your feet apart, in line with your hips, and your arms by the side of your body.

2.) Fold your knees, take your hands backward, and hold your ankles.

3.) Breathe in, and lift your chest off the ground and pull your legs up and towards the back. 

4.) Look straight ahead with a smile on your face.

5.) Keep the pose stable while paying attention to your breath. Your body is now curved and as taut as a bow.

6.) Continue to take long, deep breaths as you relax in this pose. But, bend only as far as your body permits you to.

7.) Do not overdo the stretch.

8.) After 15 -20 seconds, as you exhale, gently bring your legs and chest to the ground. Release the ankles and relax.""",fill="white", font=('Helvetica 15 bold'))

root.mainloop()