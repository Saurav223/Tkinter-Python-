from tkinter import *
root = Tk()
root.geometry('455x233')
root.title('TKinter GUI')
root.wm_iconbitmap('background.png')  # it set the icon on the title
root.configure(background='red')

width = root.winfo_screenwidth() #it return height and width of the screen
height = root.winfo_screenheight()

Button(text='Quit',command=root.destroy).pack()  # .destory function distroy the entire window


root.mainloop()
