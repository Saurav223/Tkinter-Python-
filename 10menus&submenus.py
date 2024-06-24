from tkinter import *
root = Tk()

def myfunc():
    print("my function")
root.geometry('733x566')
root.title('Menus')

#use these to create a non dropdown menu
#mymenu = Menu(root)
#mymenu.add_command(label="File",command=myfunc)
#mymenu.add_command(label="Exit",command=quit)
#root.config(menu=mymenu)


yourmenu = Menu(root)
m1 =Menu(yourmenu,tearoff=0)  #tearoff=0 disable the feature of tearing of meanu in anpther window
m1.add_command(label='Save',command=myfunc)
m1.add_command(label='Save as',command=myfunc)
m1.add_separator()  #it appear a horizontal line between the menu for seperating the option
m1.add_command(label='print',command=myfunc)
m1.add_command(label='new',command=myfunc)
root.config(menu=yourmenu)
yourmenu.add_cascade(label='File',menu=m1)



root.mainloop()