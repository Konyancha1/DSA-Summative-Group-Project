import ast
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("E-commerce Order App")
root.geometry("1280x720")
title = Label(root, text='Online Shirt Order App', bg='white', fg='black',
              font=('Montserrat', 30, 'bold'), relief=GROOVE, bd=12)
title.pack(fill=X)

Frame_1 = Frame(root, relief=RIDGE, bd=10, bg='black')
Frame_1.place(x=10, y=80, width=650, height=530)

Frame_2 = Frame(root, bg="white", relief=RIDGE, bd=10)
Frame_2.place(x=665, y=80, width=610, height=530)

name = StringVar()
address = StringVar()
email = StringVar()
shirt = StringVar()
size = StringVar()
number = IntVar()

lbl_1 = Label(Frame_1, text="Enter Full name:", font=('Montserrat', 15, 'bold'), fg='white',
              bg='black')
lbl_1.grid(row=0, column=0, padx=30, pady=10)
txt_1 = Entry(Frame_1, font=('Montserrat', 15, 'bold'), relief=RIDGE, bd=7, textvariable=name)
txt_1.grid(row=0, column=1, pady=10, sticky='w')

lbl_2 = Label(Frame_1, text="Enter Your Address:", font=('Montserrat', 15, 'bold'), fg='white',
              bg='black')
lbl_2.grid(row=1, column=0, padx=30, pady=10)
txt_2 = Entry(Frame_1, font=('Montserrat', 15, 'bold'), relief=RIDGE, bd=7, textvariable=address)
txt_2.grid(row=1, column=1, pady=10, sticky='w')

lbl_3 = Label(Frame_1, text="Enter Your Email:", font=('Montserrat', 15, 'bold'), fg='white',
              bg='black')
lbl_3.grid(row=2, column=0, padx=30, pady=10)
txt_3 = Entry(Frame_1, font=('Montserrat', 15, 'bold'), relief=RIDGE, bd=7, textvariable=email)
txt_3.grid(row=2, column=1, pady=10, sticky='w')

lbl_4 = Label(Frame_1, text="Choose Shirt Type:", font=('Montserrat', 15, 'bold'), fg='white',
              bg='black')
lbl_4.grid(row=3, column=0, padx=30, pady=10)
combo_1 = ttk.Combobox(Frame_1, font=('Montserrat', 15), state='readonly', textvariable=shirt)
combo_1['value'] = ('Plain', 'Floral', 'Short Sleeve Shirt', 'Flannel Shirt', 'Dress Shirt')
combo_1.grid(row=3, column=1, pady=10)

lbl_5 = Label(Frame_1, text="Choose Your Size:", font=('Montserrat', 15, 'bold'), fg='white',
              bg='black')
lbl_5.grid(row=4, column=0, padx=30, pady=10)
combo_2 = ttk.Combobox(Frame_1, font=('Montserrat', 15), state='readonly', textvariable=size)
combo_2['value'] = ('X-Large', 'Large', 'Medium', 'Small', 'X-Small')
combo_2.grid(row=4, column=1, pady=10)

hashed_dict = {} # creating a global variable to
def hashmap():
    global hashed_dict
    user = name.get()
    user_address = address.get()
    user_email = email.get()
    shirt_type = shirt.get()
    shirt_size = size.get()
    # Creating our dictionary
    order_dict = {}
    for variables in ["user", "user_address", "user_email", "shirt_type", "shirt_size"]:
        order_dict[variables] = eval(variables)

    order_no = random.randint(0, 1000)

    # hashed_dict = {}
    # Creating a random number to identify orders
    # while order_no in hashed_dict:

    while order_no in hashed_dict:
        order_no = random.randint(0, 1000)

    msg.config(text="Your Order Number is " + str(order_no))
    hashed_dict = {order_no: order_dict}
    # print(hashed_dict)
    # return hashed_dict


def filing():
    global hashed_dict
    order_data = open("order_data.txt", 'a')
    order_data.write(str(hashed_dict))
    order_data.write("\n")
    order_data.close()


# How the customer tracks the order
def orderProgress():
    # Collecting the order number inputed by the user
    order_no = number.get()
    # order_no = 531

    # Opening our file system where all the orders have been stored
    order_details = open("order_data.txt", 'r')
    # Looping through it then converting it to a dictionary
    for no in order_details.readlines():
        values = ast.literal_eval(no)
        if order_no in values.keys():  # Find out if the order number exists in our system.

            Frame_4 = Frame(root, bg="black", relief=RIDGE, bd=10)
            Frame_4.place(x=10, y=80, width=1260, height=530)

            view = Label(Frame_4, font=('Montserrat', 20, 'bold'), fg='black',
                        bg='white')
            view.grid(row=0, column=0, padx=150, pady=10)
            view_0 = Label(Frame_4, font=('Montserrat', 20, 'bold'), fg='black',
                         bg='white')
            view_0.grid(row=1, column=0, padx=150, pady=10)

            view.config(text='Your order is being Processed')
            view_0.config(text="Here are your Details")
            count = 2
            # Looping through the dictionary and assigning values to be printed
            print(values[order_no].keys())
            for n, k in values[order_no].items():
                view_1 = Label(Frame_4, font=('Montserrat', 15, 'bold'), fg='black',
                              bg='white')
                view_1.grid(row =count, column=0, padx=30, pady=10)
                view_1.config(text=n + "    " + k)
                count += 1
        else:
            pass
            # err.config(text="We dont have that order in our system")
            # err = messagebox.askquestion("We don't have that order in our system", "Do you want to qut?")
            # if err == "Yes":
            #     root.quit()
            # messagebox.Message("We dont have that order in our system")
    order_details.close()



# orderProgress()


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

    check_button = Button(Frame_3, text='Check Order', font=('Arial', 15, 'bold'), bg='yellow',
                          fg='black', width=20, command=check)
    check_button.grid(row=0, column=1, padx=130, pady=15)

    # txt_file = open("order.txt", "w")
    # txt_file.write("Customer name: " + str(user))
    # txt_file.write("\nCustomer Address: " + str(user_address))
    # txt_file.write("\nCustomer Contact: " + str(user_email))
    # txt_file.write("\nShirt Type: " + str(shirt_type))
    # txt_file.write("\nShirt Size: " + str(shirt_size))
    # txt_file.close()
    hashmap()
    filing()


def ask():
    ans = messagebox.askquestion("Confirm Exit", "Do you really want to exit?")
    if ans == "yes":
        root.quit()


def check():
    Frame_4 = Frame(root, bg="black", relief=RIDGE, bd=10)
    Frame_4.place(x=10, y=80, width=1260, height=530)
    lbl = Label(Frame_4, text="Enter Order Number:", font=('Montserrat', 15, 'bold'), fg='white',
                bg='black')
    lbl.grid(row=0, column=0, padx=30, pady=10)
    txt = Entry(Frame_4, font=('Montserrat', 15, 'bold'), relief=RIDGE, bd=7, textvariable=number)
    txt.grid(row=0, column=1, pady=10, sticky='w')
    enter = Button(Frame_4, text='Submit', font=('Arial', 12, 'bold'), bg='yellow',
                   fg='black', command=orderProgress)
    enter.grid(row=0, column=2, padx=10, pady=15)

    def back():
        Frame_1.tkraise()
        Frame_2.tkraise()
        Frame_4.destroy()

    back = Button(Frame_3, text='Go Back', font=('Arial', 15, 'bold'), bg='yellow',
                  fg='black', command=back, width=20)
    back.grid(row=0, column=2, padx=10, pady=15)
    Frame_4.tkraise()


msg = Label(Frame_2, font=('Montserrat', 20, 'bold'), fg='black',
            bg='white')
msg.grid(row=8, column=0, padx=150, pady=10)
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

button_2 = Button(Frame_3, text='Exit', font=('Arial', 15, 'bold'), bg='yellow', fg='black', width=20,
                  command=ask)
button_2.grid(row=0, column=3, padx=130, pady=15)

root.mainloop()
