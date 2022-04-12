from tkinter import *
from tkinter import ttk
import os

root = Tk()
root.title("E-commerce Order App")
root.geometry("1280x720")

title = Label(root, text='Online Shirt Order App', bg='white', fg='black',
              font=('Montserrat', 35, 'bold'), relief=GROOVE, bd=12)
title.pack(fill=X)

Frame_1 = Frame(root, bg="white", relief=RIDGE, bd=10)
Frame_1.place(x=10, y=80, width=650, height=530)

Frame_2 = Frame(root, bg="white", relief=RIDGE, bd=10)
Frame_2.place(x=665, y=80, width=610, height=530)

name = StringVar()
address = StringVar()
email = StringVar()
shirt = StringVar()
size = StringVar()

lbl_1 = Label(Frame_1, text="Enter Full name:", font=('Montserrat', 20, 'bold'), fg='black',
              bg='white')
lbl_1.grid(row=0, column=0, padx=30, pady=10)
txt_1 = Entry(Frame_1, font=('Montserrat', 15, 'bold'), relief=RIDGE, bd=7, textvariable=name)
txt_1.grid(row=0, column=1, pady=10, sticky='w')

lbl_2 = Label(Frame_1, text="Enter Your Address:", font=('Montserrat', 20, 'bold'), fg='black',
              bg='white')
lbl_2.grid(row=1, column=0, padx=30, pady=10)
txt_2 = Entry(Frame_1, font=('Montserrat', 15, 'bold'), relief=RIDGE, bd=7, textvariable=address)
txt_2.grid(row=1, column=1, pady=10, sticky='w')

lbl_3 = Label(Frame_1, text="Enter Your Email:", font=('Montserrat', 20, 'bold'), fg='black',
              bg='white')
lbl_3.grid(row=2, column=0, padx=30, pady=10)
txt_3 = Entry(Frame_1, font=('Montserrat', 15, 'bold'), relief=RIDGE, bd=7, textvariable=email)
txt_3.grid(row=2, column=1, pady=10, sticky='w')

lbl_4 = Label(Frame_1, text="Choose Shirt Type:", font=('Montserrat', 20, 'bold'), fg='black',
              bg='white')
lbl_4.grid(row=3, column=0, padx=30, pady=10)
combo_1 = ttk.Combobox(Frame_1, font=('Montserrat', 15), state='readonly', textvariable=shirt)
combo_1['value'] = ('Plain', 'Floral', 'Short Sleeve Shirt', 'Flannel Shirt', 'Dress Shirt')
combo_1.grid(row=3, column=1, pady=10)

lbl_5 = Label(Frame_1, text="Choose Your Size:", font=('Montserrat', 20, 'bold'), fg='black',
              bg='white')
lbl_5.grid(row=4, column=0, padx=30, pady=10)
combo_2 = ttk.Combobox(Frame_1, font=('Montserrat', 15), state='readonly', textvariable=size)
combo_2['value'] = ('X-Large', 'Large', 'Medium', 'Small', 'X-Small')
combo_2.grid(row=4, column=1, pady=10)


def output():
    user = name.get()
    user_address = address.get()
    user_email = email.get()
    shirt_type = shirt.get()
    shirt_size = size.get()
    out.config(text='Customer Order Details')
    out_1.config(text='Customer Name: ' + str(user))
    out_2.config(text='Customer Address: ' + str(user_address))
    out_3.config(text='Customer Contact: ' + str(user_email))
    out_4.config(text='Shirt Type: ' + str(shirt_type))
    out_5.config(text='Shirt Size: ' + str(shirt_size))


out = Label(Frame_2, font=('Montserrat', 20, 'bold'), fg='black',
            bg='white')
out.grid(row=0, column=0, padx=150, pady=10)
out_1 = Label(Frame_2, font=('Montserrat', 15, 'bold'), fg='black',
              bg='white')
out_1.grid(row=1, column=0, padx=30, pady=10)
out_2 = Label(Frame_2, font=('Montserrat', 15, 'bold'), fg='black',
              bg='white')
out_2.grid(row=2, column=0, padx=30, pady=10)
out_3 = Label(Frame_2, font=('Montserrat', 15, 'bold'), fg='black',
              bg='white')
out_3.grid(row=3, column=0, padx=30, pady=10)
out_4 = Label(Frame_2, font=('Montserrat', 15, 'bold'), fg='black',
              bg='white')
out_4.grid(row=4, column=0, padx=30, pady=10)
out_5 = Label(Frame_2, font=('Montserrat', 15, 'bold'), fg='black',
              bg='white')
out_5.grid(row=5, column=0, padx=30, pady=10)

Frame_3 = Frame(root, bg="white", relief=RIDGE, bd=15)
Frame_3.place(x=10, y=615, width=1260, height=100)

button_1 = Button(Frame_1, text='Submit Order', font=('Arial', 15, 'bold'), bg='yellow', fg='black', width=20,
                  command=output)
button_1.grid(row=5, column=1, pady=10)

button_2 = Button(Frame_3, text='Add Order', font=('Arial', 15, 'bold'), bg='yellow', fg='black', width=10)
button_2.grid(row=0, column=1, padx=250, pady=15)

button_3 = Button(Frame_3, text='Exit', font=('Arial', 15, 'bold'), bg='yellow', fg='black', width=10)
button_3.grid(row=0, column=3, padx=230, pady=15)

root.mainloop()
