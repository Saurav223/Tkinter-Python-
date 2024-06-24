from tkinter import *

root = Tk()
root.geometry('655x333')
def getvalues():
    print(uservalue.get())
    print(passvalue.get())
user =Label(root,text='Username')
password = Label(root,text="Password")
user.grid()   #packing (its arguments are row and columb)
password.grid(row=1)

#variable class in Tkinter
#BooleanVar, DOubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root,textvariable=uservalue)
passentry = Entry(root,textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit",command=getvalues).grid()

root.mainloop()