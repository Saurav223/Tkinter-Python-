from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('455x233')
root.title('Radio Button')

def func():
    messagebox.showinfo('Food',f'You have order {food[var.get()-1]}')

var = IntVar()
Label(root,text='What would you like to have sir',font='lucida 19 bold',justify=LEFT,padx=14).pack()

food = ['Momo','Chaumin','Samosa','Pizza','Burger']
j = 0
for i in food:
    j+=1
   # radio = Radiobutton(root,text=i,padx=14,variable=var,value=j).pack(anchor ='w')
    Radiobutton(root,text=i,padx=14,variable=var,value=j).pack(anchor ='w')

Button(root,text='Submit',command=func).pack()


root.mainloop()