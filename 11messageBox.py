from tkinter import *
from tkinter import messagebox
root = Tk()

def myfunc():
    print("my function")
root.geometry('733x566')
root.title('Menus')

def help():
    print('Help function')
    messagebox.showinfo('Help','God will help you my boy')

def rate():
    a = messagebox.askquestion("Rate")
    
yourmenu = Menu(root)
m1 =Menu(yourmenu,tearoff=0)  #tearoff=0 disable the feature of tearing of meanu in anpther window
m1.add_command(label='Save',command=myfunc)
m1.add_command(label='Save as',command=myfunc)
m1.add_separator()  #it appear a horizontal line between the menu for seperating the option
m1.add_command(label='print',command=myfunc)
m1.add_command(label='new',command=myfunc)
root.config(menu=yourmenu)
yourmenu.add_cascade(label='File',menu=m1)


m2 =Menu(yourmenu,tearoff=0)  #tearoff=0 disable the feature of tearing of meanu in anpther window
m2.add_command(label='Cut',command=myfunc)
m2.add_command(label='Copy',command=myfunc)
m2.add_separator()  #it appear a horizontal line between the menu for seperating the option
m2.add_command(label='Paste',command=myfunc)
m2.add_command(label='Find',command=myfunc)
root.config(menu=yourmenu)
yourmenu.add_cascade(label='Edit',menu=m2)

m3 = Menu(yourmenu,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label='Rate',command=rate)
root.config(menu=yourmenu)
yourmenu.add_cascade(label="Help",menu=m3)


root.mainloop()