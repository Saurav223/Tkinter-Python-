from tkinter import *
root = Tk()

def func(event):
    print(f'button clicked {event.x}, {event.y}')

root.title('Event Handling')
root.geometry('644x234')

widget = Button(root, text='Click')
widget.pack()

widget.bind('<Button-1>',func)
widget.bind('<Double-1>,quit')

root.mainloop()