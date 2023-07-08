import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re


##############################################+=============================================================
root = tk.Tk()
root.configure(background="black")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("1920x1080+200+50")
root.title("Login Form")




username = tk.StringVar()
password = tk.StringVar()
        

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('plane.jpg')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relw#idth=1, relheight=1)


#image2 =Image.open('I5.jpg')
#mage2 =image2.resize((750,890), Image.ANTIALIAS)

#background_image=ImageTk.PhotoImage(image2)
#background_label = tk.Label(root, image=background_image)

#background_label.image = background_image

#background_label.place(x=0, y=0) 



def registration():
    from subprocess import call
    call(["python","registration.py"])
    root.destroy()

def login():
        # Establish Connection

    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS admin_registration"
                           "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM admin_registration WHERE username = ? and password = ?')
         c.execute(find_entry, [(username.get()), (password.get())])
         result = c.fetchall()

         if result:
            msg = ""
            # self.logf.pack_forget()
            # self.head['text'] = self.username.get() + '\n Loged In'
            # msg = self.head['text']
            #            self.head['pady'] = 150
            print(msg)
            ms.showinfo("messege", "LogIn sucessfully")
            # ===========================================
            

            from subprocess import call
            call(['python','Home.py'])
            root.destroy()
            # ================================================
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')

def Login():

    from subprocess import call
    call(["python", "Home.py"])  
   

title=tk.Label(root, text="Login Here", font=("Algerian", 30, "bold","italic"),bd=5,bg="white",fg="black")
title.place(x=700,y=200,width=250)
        
# Login_frame=tk.Frame(root,bg="white")
# Login_frame.place(x=900,y=300)
frame=tk.Frame(root,width=550,height=400,bg="gray")
frame.place(x=545,y=300)
logolbl=tk.Label(frame,bd=0).grid(row=0,columnspan=2,pady=20)
        
lbluser=tk.Label(frame,text="Username",compound=LEFT,font=("Times new roman", 20, "bold"),bg="#D3D3D3").grid(row=1,column=0,padx=20,pady=10)
txtuser=tk.Entry(frame,bd=5,border=0,textvariable=username,font=("",15))
txtuser.grid(row=1,column=1,padx=20)
tk.Frame(frame,width=200,height=2,bg='black').place(x=220,y=400)
     
lblpass=tk.Label(frame,text="Password",compound=LEFT,font=("Times new roman", 20, "bold"),bg="#D3D3D3").grid(row=2,column=0,padx=50,pady=10)
txtpass=tk.Entry(frame,bd=5,border=0,textvariable=password,show="*",font=("",15))
txtpass.grid(row=2,column=1,padx=20)
tk.Frame(frame,width=200,height=2,bg='black').place(x=220,y=550)
        
btn_log=tk.Button(frame,text="Login",command=login,width=15,font=("Times new roman", 14, "bold"),bg="black",fg="white")
btn_log.grid(row=4,column=0,pady=10)
btn_reg=tk.Button(frame,text="Create Account",command=registration,width=15,font=("Times new roman", 14, "bold"),bg="black",fg="white")
btn_reg.grid(row=4,column=1,pady=10)
btn_reg=tk.Button(frame,text="Back",command=Login,width=10,font=("Times new roman", 14, "bold"),bg="red",fg="black")
btn_reg.grid(row=4,column=2,pady=10)
        
       

root.mainloop()