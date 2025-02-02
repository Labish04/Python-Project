from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import subprocess

def login():
    if username_entry.get()=="" or password_entry.get()=="":
        messagebox.showerror("Error","All fields are required")
    elif username_entry.get()=="asdf" and password_entry.get()=="jkl;":
        messagebox.showinfo("Success","Login Successful")
        win.destroy()
        subprocess.run(['python','menu.py'])

    else:
        messagebox.showerror("Error","Wrong username or password")
        
def toggle_password():
    if var.get() == 1:
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

def login_on_enter(e):
    login_button.config(bg='#fc0303',
                  fg='black')
    
def login_on_leave(e):
    login_button.config(bg='#d40707',
                  fg='black')

#window
win = Tk()
win.title("Instant Order")
win.geometry("1920x1080")
win.configure(bg="white")
logo=PhotoImage(file="instantorder_logowithoutbg.png")
win.iconphoto(True, logo)

#Logo Image
logo_image= PhotoImage(file='instantorder_logo.png')
original_logo_image = Image.open("instantorder_logo.png")
resized_logo_image = original_logo_image.resize((800, 600), Image.Resampling.LANCZOS)
logo_image = ImageTk.PhotoImage(resized_logo_image)
logo_label = Label(win, image=logo_image, bg="white")
logo_label.place(x=30, y=-150)

#Place your order in an instant
slogan = Label(win,
                    text="Place your order in an instant",
                    font=("Arial", 20, 'italic'),
                    bg="white",
                    fg="black",)
slogan.place(x=220, y=250)

#Discription
discription1= Label(win, text='"Instant Order" is a simple and efficient application that',
                   font= ('Arial', 15, 'italic'),
                   bg='white',
                   fg='black')
discription1.place(x=100, y=400)

discription2= Label(win, text='allows you to place orders directly from a predefined menu.',
                   font= ('Arial', 15, 'italic'),
                   bg='white',
                   fg='black')
discription2.place(x=100, y=440)

discription3= Label(win, text='With just a few taps, you can select your items, confirm',
                    font= ('Arial', 15, 'italic'),
                   bg='white',
                   fg='black')
discription3.place(x=100, y=480)

discription4= Label(win, text='your order, and receive an instant bill.',
                    font= ('Arial', 15, 'italic'),
                   bg='white',
                   fg='black')
discription4.place(x=100, y=520)

discription5= Label(win, text='No hassle, no waiting—just quick and seamless ordering!',
                    font= ('Arial', 15, 'italic'),
                   bg='white',
                   fg='black')
discription5.place(x=100, y=560)

#username
username=Label(win,
                text="Username:",
                font=("Arial", 30,),
                bg="white",
                fg="black",)
username.place(x=900, y=400)
username_entry = Entry(win,
                           font=("Arial", 20,),
                           width=20,
                           highlightthickness=2,
                           highlightbackground='red',
                           highlightcolor='red')
username_entry.place(x=1100, y=407)

#password
password=Label(win,
                text="Password:",
                font=("Arial", 30,),
                bg="white",
                fg="black",)
password.place(x=900, y=480)
password_entry = Entry(win,
                           show="*",
                           font=("Arial", 20,),
                           width=20,
                           highlightthickness=2,
                           highlightbackground= 'red',
                           highlightcolor='red')
password_entry.place(x=1100, y=487)

#show
var=IntVar()
show=Checkbutton(win,
                 text="show", variable=var, command=toggle_password)
show.place(x=1420, y=495)

#Login
login_button = Button(win,
                text="Login",
                font=("Arial", 25,'bold'),
                bg="#d40707",
                fg="black",
                activeforeground='black',
                activebackground='#fc0303',
                command= login,
                padx=50,
                pady=0)
login_button.place(x=1150, y=565)
login_button.bind("<Enter>", login_on_enter)
login_button.bind("<Leave>", login_on_leave)

mainloop()