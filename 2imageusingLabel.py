from tkinter import *
from PIL import Image
root = Tk()
root.geometry('512x640')
photo1 = PhotoImage(file ='background.png')
label1 = Label(image = photo1)
label1.pack()

root.mainloop()