from tkinter import *
root = Tk()
root.title("Calculator")
n=Label(root,text="First Number")
p=Label(root,text="Second Number")
c=Label(root,text="Enter the operation")
n.grid(row=1,column=2)
p.grid(row=2,column=2)
c.grid(row=3,column=2)
ne=IntVar()
pe=IntVar()
cmp=StringVar()
a=Entry(root,textvariable=ne)
b=Entry(root,textvariable=pe)
cm=Entry(root,textvariable=cmp)
a.grid(row=1,column=3)
b.grid(row=2,column=3)
cm.grid(row=3,column=3)
pr=Label(root,text=" for addition press add"
      "  for subtraction press sub"
      "  for multiplication press mul"
      "  for division press div")
pr.grid(row=4,column=2)

def getvals():
    cmd=cmp.get()
    a1=int(ne.get())
    a2=int(pe.get())
    if cmd=="add":
        s="Addition"+" is "+str(a1+a2)
        l=Label(root,text=s)
        l.grid(row=6,column=1)
    elif cmd=="sub":
        s ="Substraction" + " is " + str(a1 - a2)
        l = Label(root, text=s)
        l.grid(row=6, column=1)
    elif cmd=="mul":
         s = "Multiplication" + " is " + str(a1 * a2)
         l = Label(root, text=s)
         l.grid(row=6, column=1)
    elif cmd=="div":
          s = "Division" + " is " + str(a1 / a2)
          l = Label(root, text=s)
          l.grid(row=6, column=1)
    else:
          s="invalid command"
          l = Label(root, text=s)
          l.grid(row=6, column=1)
Button(text="Operate",command=getvals).grid(row=5,column=2)
mainloop()