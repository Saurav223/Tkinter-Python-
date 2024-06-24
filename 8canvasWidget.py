from tkinter import *
root = Tk()

canvasWidth = 800
canvasHeight = 400
root.geometry(f'{canvasWidth}x{canvasHeight}')

can_widget = Canvas(root,width=canvasWidth,height=canvasWidth)
can_widget.pack()

#The line goes form the point x1, y1 to x2, y2
can_widget.create_line(100,200,700,0,fill="red")

can_widget.create_rectangle(100,200,300,400)

can_widget.create_text(200,200, text="python",fill='red',font='comicsanms 13 bold')
root.mainloop()