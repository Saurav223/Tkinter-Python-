from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('455x233')
root.title('Slider')

def func():
    print(f'Your level is {myslider.get()}')
    messagebox.showinfo('INFO',f'level is {myslider.get()} ')

#myslider = Scale(root,from_=0, to=5)
#myslider.pack()
itm = StringVar
Label(root,text='Whants your level?').pack()
myslider = Scale(root,from_=0, to=5, orient=HORIZONTAL)
myslider.set(4)
myslider.pack()
Button(root,text='Button',command = func).pack()

root.mainloop()