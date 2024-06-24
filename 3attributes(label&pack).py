from tkinter import *
root = Tk()
root.geometry('444x233')
root.title('My GUI')

# IMP label option
#text - adds the Text
#bd - background
#fg - foreground
#font - sets the font
#1.font=('comicsansms',19,'bold')
#2.font= 'comicsansms 19 bold'
#padx - x padding
#pady - y padding
#relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

titlelabel = Label(text ='''Nepal,[a] officially the Federal Democratic Republic of Nepal,[b] is a landlocked country 
in South Asia. It is mainly situated in the Himalayas,
but also includes parts of the Indo-Gangetic Plain. 
It borders the Tibet Autonomous Region of China to the north,
and India to the south, east, and west,
while it is narrowly separated from Bangladesh by the Siliguri Corridor, 
and from Bhutan by the Indian state of Sikkim. Nepal has a diverse geography, including
fertile plains, subalpine forested hills, and eight of the world's ten tallest mountains, 
including Mount Everest, the highest point on Earth. Kathmandu is the nation's
capital and the largest city. Nepal is a multi-ethnic, multi-lingual, multi-religious 
and multi-cultural state, with Nepali as the official language.
''',bg ='red',fg='white',padx=113,pady=94,font='comicsansms 19 bold',
relief=GROOVE)

# IMP pack option
# anchor = nw(north west)
# side = top, bottom, left, right
# fill
# padx
# pady

#titlelabel.pack(anchor='sw')
#titlelabel.pack(side=BOTTOM,anchor='sw')
#titlelabel.pack(side=BOTTOM,anchor='sw',fill=X)
titlelabel.pack(side=LEFT,fill=Y,padx=20,pady=20)


root.mainloop()