import socket
from tkinter import *

def send(listbox,entry):
    message = entry.get()
    listbox.insert('end',message)
    entry.delete(0,END)
    s.send(bytes(message, "utf-8"))
    receive(listbox)

def receive(listbox):
    message = s.recv(50)
    listbox.insert('end',"Server:"+message.decode('utf-8'))

root = Tk()

entry = Entry()
entry.pack(side=BOTTOM)

listBox = Listbox(root)
listBox.pack()

button = Button(root,text="Send",command=lambda: send(listBox,entry))
button.pack(side=BOTTOM)

rbutton = Button(root,text="Receive",command=lambda: send(listBox))
rbutton.pack(side=BOTTOM)
root.title('Client')

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12345

s.connect((HOST_NAME,PORT))

root.mainloop()
