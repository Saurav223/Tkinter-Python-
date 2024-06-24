from tkinter import *
root = Tk()
root.geometry('655x333')
f1 = Frame(root,bg ='grey', borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")

f2 = Frame(root,borderwidth=8,bg='grey',relief=SUNKEN)
f2.pack(side=TOP, fill='x')
l = Label(f1,text='Project Tkinter - Pycharm')
l.pack()

l = Label(f2,text='WELCOM TO THE SUBLIME TEXT',font='Helvetica 16 bold',bg='grey',fg='red')
l.pack()

root.mainloop()