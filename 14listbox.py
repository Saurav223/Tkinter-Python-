from tkinter import *
root = Tk()
root.geometry('455x233')
root.title('ListBox')

def add():
    lbx.insert(END,i.get())
    i.set("")

i = StringVar()
Entry(root,textvariable=i).pack()
lbx = Listbox(root)
lbx.pack()
lbx.insert(END,'First item of list')

Button(root,text='Add Item',command=add).pack()

root.mainloop()