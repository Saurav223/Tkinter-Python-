from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('744x344')

    def status(self):
        self.var = StringVar()
        self.var.set('Ready')
        self.statusbar = Label(self,textvariable=self.var,relief=SUNKEN,anchor='w')
        self.statusbar.pack(side=BOTTOM,fill=X)

    def createbutton(self,inputext):
        Button(text=inputext,command=self.click).pack()

    def click(self):
        print('Button Clicked')

if __name__ == '__main__':
    window = GUI()
    window.status()
    window.createbutton('Click')
    window.createbutton('Submit')
    window.mainloop()
