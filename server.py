#Importing modules
import socket

#Tkinter for UI support
from tkinter import *

#Sending a message
def send(listbox,entry):
    message = entry.get()
    listbox.insert('end',message)
    entry.delete(0,END)
    client.send(bytes(message, "utf-8"))

#Receiving a message
def receive(listbox):
    message_from_client = client.recv(50)
    listbox.insert('end',"Client:"+message_from_client.decode('utf-8'))

#Root Window
root = Tk()

#Input Buttom
entry = Entry()
entry.pack(side=BOTTOM)

listBox = Listbox(root)
listBox.pack()

#Send Button
button = Button(root,text="Send",command=lambda: send(listBox,entry))
button.pack(side=BOTTOM)

#Receive Button
rbutton = Button(root,text="Receive",command=lambda: receive(listBox))
rbutton.pack(side=BOTTOM)
root.title('Server')

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12345

s.bind((HOST_NAME,PORT))

s.listen(4)
client,address = s.accept()

#Starting of event loop
root.mainloop()

