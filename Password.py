from tkinter import *
import random
import string
root = Tk()
root.geometry("1255x944")
root.title("Calculator")
n = Label(root, text="Enter length of password:")
n.grid(row=1, column=2)
ne = IntVar()
a = Entry(root, textvariable=ne)
a.grid(row=1, column=3)
def passw():
    np=int(ne.get())
    digi= string.digits
    letter = string.ascii_letters
    p=random.sample((letter+digi),k=np)
    string_result = "".join(str(x) for x in p)
    kl=Label(root,text="Recommended password is:")
    kl.grid(row=2,column=2)
    l=Label(root,text=string_result)
    l.grid(row=2,column=3)
Button(text="Operate",command=passw).grid(row=4,column=2)
mainloop()
