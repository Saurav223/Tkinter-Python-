from tkinter import *
root = Tk()  #making instense of TK class (root)
# Width x Height
root.geometry('600x600')

#width, heigth
root.minsize(200,200)
root.maxsize(700,700)

label1 = Label(text='Hello it is the label')
label1.pack()
root.mainloop()

