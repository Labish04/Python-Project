from tkinter import *
from PIL import ImageTk, Image
def placeorder_on_enter(e):
    place_order.config(bg='#fc0303',
                  fg='black')
    
def placeorder_on_leave(e):
    place_order.config(bg='#d40707',
                  fg='black')

#window
root = Tk()
root.title('Instant Order')
root.geometry('1920x1080')
root.config(bg='white')
logo = PhotoImage(file='instantorder_logowithoutbg.png')
root.iconphoto(True, logo)

#Border
canvas = Canvas(root, width=1920, height=1080, bg='white', highlightthickness=0)
canvas.pack()
canvas.create_rectangle(20, 100, 1510, 700, outline='#d40707', width=5, dash=(5,2))

#Logo Mark
logo_image= PhotoImage(file='instantorder_logo.png')
original_logo_mark = Image.open('instantorder_logo.png')
resized_logo_mark = original_logo_mark.resize((120, 120), Image.Resampling.LANCZOS)
logo_mark= ImageTk.PhotoImage(resized_logo_mark)
logo_mark_label = Label(root, image = logo_mark, bg='white')
logo_mark_label.place(x=0, y=-25)

#Menu
menu= Label(root,
            text='MENU',
            font=('Goudy Old Style', 35, 'bold'),
             fg='white',
             bg='#d40707',
             padx=600,
             pady=0)
menu.place(x=95, y=120)

#Hot Drinks
hot_drinks = Label(root,
                   text='Hot Drinks',
                   font=('Goudy Old Style',25, 'bold'),
                   fg='#d40707',
                   bg='white')
hot_drinks.place(x=190, y=200)

#milk tea
milk_tea= Label(root,
                text='Milk Tea..................',
                font=('Arial', 18),
                fg='black',
                bg='white')
milk_tea.place(x=190, y=240)

milk_tea_price= Label(root,
                text='Rs. 25',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
milk_tea_price.place(x=410, y=240)

milk_tea_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
milk_tea_sb.place(x=500, y=245)

#black tea
black_tea= Label(root,
                text='Black Tea................',
                font=('Arial', 18),
                fg='black',
                bg='white')
black_tea.place(x=190, y=280)

black_tea_price= Label(root,
                text='Rs. 20',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
black_tea_price.place(x=410, y=280)

black_tea_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
black_tea_sb.place(x=500, y=285)

#hot  lemon
hot_lemon= Label(root,
                text='Hot Lemon...............',
                font=('Arial', 18),
                fg='black',
                bg='white')
hot_lemon.place(x=190, y=320)

hot_lemon_price= Label(root,
                text='Rs. 30',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
hot_lemon_price.place(x=410, y=320)

hot_lemon_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
hot_lemon_sb.place(x=500, y=325)

#black coffee
black_coffee= Label(root,
                text='Black Coffee............',
                font=('Arial', 18),
                fg='black',
                bg='white')
black_coffee.place(x=190, y=360)

black_coffee_price= Label(root,
                text='Rs. 40',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
black_coffee_price.place(x=410, y=360)

black_coffee_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
black_coffee_sb.place(x=500, y=365)

#milk coffee
milk_coffee= Label(root,
                text='Milk Coffee...............',
                font=('Arial', 18),
                fg='black',
                bg='white')
milk_coffee.place(x=190, y=400)

milk_coffe_price= Label(root,
                text='Rs. 50',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
milk_coffe_price.place(x=410, y=400)

milk_coffee_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
milk_coffee_sb.place(x=500, y=405)

#hot chocolate
hot_chocolate= Label(root,
                text='Hot Chocolate..........',
                font=('Arial', 18),
                fg='black',
                bg='white')
hot_chocolate.place(x=190, y=440)

hot_chocolate_price= Label(root,
                text='Rs. 90',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
hot_chocolate_price.place(x=410, y=440)

hot_chocolate_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
hot_chocolate_sb.place(x=500, y=445)

#Cold Drinks
cold_drinks = Label(root,
                   text='Cold Drinks',
                   font=('Goudy Old Style',25, 'bold'),
                   fg='#d40707',
                   bg='white')
cold_drinks.place(x=190, y=500)

#coke
coke= Label(root,
                text='Coke......................',
                font=('Arial', 18),
                fg='black',
                bg='white')
coke.place(x=190, y=540)

coke_price= Label(root,
                text='Rs. 60',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
coke_price.place(x=410, y=540)

coke_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
coke_sb.place(x=500, y=545)

#sprite
sprite= Label(root,
                text='Sprite.....................',
                font=('Arial', 18),
                fg='black',
                bg='white')
sprite.place(x=190, y=580)

sprite_price= Label(root,
                text='Rs. 60',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
sprite_price.place(x=410, y=580)

sprite_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
sprite_sb.place(x=500, y=585)

#fanta
fanta= Label(root,
                text='Fanta.....................',
                font=('Arial', 18),
                fg='black',
                bg='white')
fanta.place(x=190, y=620)

fanta_price= Label(root,
                text='Rs. 60',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
fanta_price.place(x=410, y=620)

fanta_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
fanta_sb.place(x=500, y=625)

#lassi
lassi= Label(root,
                text='Lassi......................',
                font=('Arial', 18),
                fg='black',
                bg='white')
lassi.place(x=190, y=660)

lassi_price= Label(root,
                text='Rs. 60',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
lassi_price.place(x=410, y=660)

lassi_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
lassi_sb.place(x=500, y=665)

#MoMo
momo = Label(root,
                   text='MoMo',
                   font=('Goudy Old Style',25, 'bold'),
                   fg='#d40707',
                   bg='white')
momo.place(x=900, y=200)

#veg momo
veg_momo= Label(root,
                text='Veg MoMo..................',
                font=('Arial', 18),
                fg='black',
                bg='white')
veg_momo.place(x=900, y=240)

veg_momo_price= Label(root,
                text='Rs. 100',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
veg_momo_price.place(x=1140, y=240)

veg_momo_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
veg_momo_sb.place(x=1250, y=245)

#buff momo
buff_momo= Label(root,
                text='Buff MoMo.................',
                font=('Arial', 18),
                fg='black',
                bg='white')
buff_momo.place(x=900, y=280)

buff_momo_price= Label(root,
                text='Rs. 130',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
buff_momo_price.place(x=1140, y=280)

buff_momo_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
buff_momo_sb.place(x=1250, y=285)

#chicken momo
chicken_momo= Label(root,
                text='Chicken MoMo............',
                font=('Arial', 18),
                fg='black',
                bg='white')
chicken_momo.place(x=900, y=320)

chicken_momo_price= Label(root,
                text='Rs. 150',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
chicken_momo_price.place(x=1140, y=320)

chicken_momo_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
chicken_momo_sb.place(x=1250, y=325)

#Burger
burger = Label(root,
                   text='Burger',
                   font=('Goudy Old Style',25, 'bold'),
                   fg='#d40707',
                   bg='white')
burger.place(x=900, y=370)

#chicken burger
chicken_burger= Label(root,
                text='Chicken Burger...........',
                font=('Arial', 18),
                fg='black',
                bg='white')
chicken_burger.place(x=900, y=410)

chicken_burger_price= Label(root,
                text='Rs. 310',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
chicken_burger_price.place(x=1140, y=410)

chicken_burger_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
chicken_burger_sb.place(x=1250, y=415)

#ham burger
ham_burger= Label(root,
                text='Ham Burger................',
                font=('Arial', 18),
                fg='black',
                bg='white')
ham_burger.place(x=900, y=450)

ham_burger_price= Label(root,
                text='Rs. 280',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
ham_burger_price.place(x=1140, y=450)

ham_burger_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
ham_burger_sb.place(x=1250, y=455)

#veg burger
veg_burger= Label(root,
                text='Veg Burger................',
                font=('Arial', 18),
                fg='black',
                bg='white')
veg_burger.place(x=900, y=490)

veg_burger_price= Label(root,
                text='Rs. 230',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
veg_burger_price.place(x=1140, y=490)

veg_burger_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
veg_burger_sb.place(x=1250, y=495)

#Pizza
pizza = Label(root,
                   text='Pizza',
                   font=('Goudy Old Style',25, 'bold'),
                   fg='#d40707',
                   bg='white')
pizza.place(x=900, y=540)

#chicken pizza
chicken_pizza= Label(root,
                text='Chicken Pizza(M).........',
                font=('Arial', 18),
                fg='black',
                bg='white')
chicken_pizza.place(x=900, y=580)

chicken_pizza_price= Label(root,
                text='Rs. 550',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
chicken_pizza_price.place(x=1140, y=580)

chicken_pizza_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
chicken_pizza_sb.place(x=1250, y=585)

#mushroom pizza
mushroom_pizza= Label(root,
                text='Mushroom Pizza(M)...',
                font=('Arial', 18),
                fg='black',
                bg='white')
mushroom_pizza.place(x=900, y=620)

mushroom_pizza_price= Label(root,
                text='Rs. 450',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
mushroom_pizza_price.place(x=1140, y=620)

mushroom_pizza_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
mushroom_pizza_sb.place(x=1250, y=625)

#cheese pizza
cheese_pizza= Label(root,
                text='Cheese Pizza(M).........',
                font=('Arial', 18),
                fg='black',
                bg='white')
cheese_pizza.place(x=900, y=660)

cheese_pizza_price= Label(root,
                text='Rs. 500',
                font=('Arial', 18),
                fg='#d40707',
                bg='white')
cheese_pizza_price.place(x=1140, y=660)

cheese_pizza_sb = Spinbox(from_=0, to=10, highlightbackground='#d40707', highlightthickness=2, width=3)
cheese_pizza_sb.place(x=1250, y=665)

#Place order
place_order = Button(root,
                     text='Place Order',
                     font=('Arial', 20, 'bold'),
                     fg='black',
                     bg='#d40707',
                     activeforeground='black',
                     activebackground='#fc0303',
                     padx=30,
                     pady=0)
place_order.place(x=1276, y=720)
place_order.bind('<Enter>', placeorder_on_enter)
place_order.bind('<Leave>', placeorder_on_leave)

mainloop()