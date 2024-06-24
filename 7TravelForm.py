from tkinter import *
root = Tk()
root.geometry('644x344')

def getvals():
    print('Form Submitted')
    with open("record.txt","a") as f:
      f.write(f"{namevalue.get()}, {phonevalue.get()}, {gendervalue.get()}, {emergencyvalue.get()}, {payvalue.get()}, {foodservice.get()} \n") 
    namevalue.set("")
    phonevalue.set("")
    gendervalue.set("")
    emergencyvalue.set("")
    payvalue.set("")
    foodservice.set(0) 

    confirmation_label = Label(root, text="Form submitted successfully!", fg="green")
    confirmation_label.grid(row=8, column=3)

    confirmation_label.after(2000, confirmation_label.destroy)
    return
    

Label(root, text='Welcome to the MOUNT Travels', font='comicsanms 13 bold').grid(row=0,column=3)
name = Label(root,text='Name')
phone = Label(root,text='Phone')
gender = Label(root,text='Gender')
emergency = Label(root,text='Emergency Contact')
pay = Label(root,text='Payment Mode')

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
pay.grid(row=5,column=2)

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
payvalue = StringVar()
foodservice = IntVar()

nameentry = Entry(root,textvariable=namevalue)
phoneentry = Entry(root,textvariable=phonevalue)
genderentry = Entry(root,textvariable=gendervalue)
emergencyentry = Entry(root,textvariable=emergencyvalue)
payentry = Entry(root,textvariable=payvalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
payentry.grid(row=5,column=3)

#checkbox
Checkbutton(text="Want to prebook your meals?",variable=foodservice).grid(row=6,column=3)

Button(text='Submit',command=getvals).grid(row=7,column=3)

root.mainloop()