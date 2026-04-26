from tkinter import *

def send(listBox,entry):
    message = entry.get()
    listBox.insert('end',message)
    entry.delete(0,END)

root = Tk()

entry = Entry()
entry.pack(side=BOTTOM)

listBox = Listbox(root)
listBox.pack()

button = Button(root,text="Send",command=lambda: send(listBox,entry))
button.pack(side=BOTTOM)

root.mainloop()