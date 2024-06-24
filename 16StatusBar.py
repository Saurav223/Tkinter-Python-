from tkinter import *
root = Tk()
root.geometry('455x233')
root.title('Status Bar')

def upload():
    statusvar.set('Upload')

def download():
    statusvar.set('Download')

statusvar = StringVar()
statusvar.set('Ready')
sbar = Label(root,textvariable=statusvar,relief=SUNKEN)
sbar.pack(side=BOTTOM ,fill=X)
Button(root,text='Upload',command=upload).pack()
Button(root,text='Download',command=download).pack()


root.mainloop()