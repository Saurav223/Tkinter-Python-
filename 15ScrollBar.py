from tkinter import *
root = Tk()
root.geometry('455x233')
root.title('ScrollBar')

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

listbox = Listbox(root, yscrollcommand= scrollbar.set)
for i in range(100):
    listbox.insert(END,f'Item{i}')
listbox.pack(fill='both')
scrollbar.config(command=listbox.yview)


root.mainloop()