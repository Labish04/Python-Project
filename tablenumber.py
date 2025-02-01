from tkinter import *
from PIL import ImageTk, Image

def next_on_enter(e):
    next_button.config(fg='black',
                       bg='#fc0303')

def next_on_leave(e):
    next_button.config(fg='black',
                       bg='#d40707')

#window
root1 = Tk()
root1.title('Table Number')
root1.geometry('1920x1080')
root1.configure(bg='white')
logo = PhotoImage(file='instantorder_logo.png')
root1.iconphoto(True, logo)

#Canvas
canvas = Canvas(root1, width=1920, height=1080, bg='white')
canvas.pack()
canvas.create_rectangle(300, 100, 1200, 600, outline='#d40707', width=5)

#Logo Mark
original_logo_mark = Image.open('instantorder_logo.png')
resized_logo_mark = original_logo_mark.resize((120, 120), Image.Resampling.LANCZOS)
logo_mark= ImageTk.PhotoImage(resized_logo_mark)
logo_mark_label = Label(root1, image = logo_mark, bg='white')
logo_mark_label.place(x=0, y=-25)

#Insert Your Table Number
insert_your_table_number = Label(root1, 
                     text='Inser Your Table Number', 
                     font=('Goudy Old Style', 40, 'bold'),
                     bg='#d40707',
                     fg='white',
                     padx=100)
insert_your_table_number.place(x=370, y=120)

#Table Number Entry
table_number_entry = Entry(root1,
                                 font=('Arial', 70),
                                 width=10,
                                 highlightthickness=2,
                                 highlightbackground='#d40707',
                                 highlightcolor='#d40707')
table_number_entry.place(x=470, y=330)

#Next Button
next_button = Button(root1,
                     text='Next',
                     font=('Arial', 28, 'bold'),
                     bg='#d40707',
                     fg='black',
                     activeforeground='black',
                     activebackground='#fc0303',
                     padx=80,
                     pady=-0)
next_button.place(x=1070, y=650)
next_button.bind('<Enter>',next_on_enter)
next_button.bind('<Leave>',next_on_leave)

mainloop()