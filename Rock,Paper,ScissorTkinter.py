import random
from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.title("Rock,Paper,Scissor")
root.geometry("1255x944")
a=Label(root,text="Enter your choice",fg="red")
#print("Choose rock,paper or scissor")
a.grid(row=1,column=2)
c=StringVar()
cm=Entry(root,textvariable=c)
cm.grid(row=1,column=3)
mylist=["rock","paper","scissor"]
p=random.choice(mylist)
def choice():
    cmd=str(c.get())
    print(cmd)
    global photo
    if cmd=="rock" and p=="scissor":
        Label(root,text="Computer chose").grid(row=2,column=2)
        Label(root,text=p).grid(row=2,column=3)
        image = Image.open("win.png")
        photo = ImageTk.PhotoImage(image)
        Label(image=photo).grid(row=4,column=5)
    if cmd=="paper" and p=="scissor":
        Label(root, text="Computer chose").grid(row=2, column=2)
        Label(root, text=p).grid(row=2, column=3)
        image = Image.open("lose.png")
        photo = ImageTk.PhotoImage(image)
        Label(image=photo).grid(row=4,column=5)
    if cmd=="scissor" and p=="rock":
        Label(root, text="Computer chose").grid(row=2, column=2)
        Label(root, text=p).grid(row=2, column=3)
        image = Image.open("lose.png")
        photo = ImageTk.PhotoImage(image)
        Label(image=photo).grid(row=4,column=5)
    if cmd=="rock" and p=="paper":
        Label(root, text="Computer chose").grid(row=2, column=2)
        Label(root, text=p).grid(row=2, column=3)
        image = Image.open("lose.png")
        photo = ImageTk.PhotoImage(image)
        Label(image=photo).grid(row=4,column=5)
    if cmd=="paper" and p=="rock":
        Label(root, text="Computer chose").grid(row=2, column=2)
        Label(root, text=p).grid(row=2,column=3)
        image = Image.open("win.png")
        photo = ImageTk.PhotoImage(image)
        Label(image=photo).grid(row=4,column=5)
    if cmd=="scissor" and p=="paper":
        Label(root, text="Computer chose").grid(row=2, column=2)
        Label(root, text=p).grid(row=2, column=3)
        image = Image.open("win.png")
        photo = ImageTk.PhotoImage(image)
        Label(image=photo).grid(row=4,column=5)
    if cmd==p:
        Label(root, text="Computer chose").grid(row=2, column=2)
        Label(root, text=p).grid(row=2, column=3)
        image = Image.open("Draw.png")
        photo = ImageTk.PhotoImage(image)
        Label(image=photo).grid(row=4,column=5)
Button(text="Execute",command=choice).grid(row=3,column=2)
mainloop()
