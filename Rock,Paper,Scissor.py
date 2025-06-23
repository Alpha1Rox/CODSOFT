import random
mylist=["rock","paper","scissor"]
for x in iter(int, 1):
    cmd = input("Enter your choice:")
    p = random.choice(mylist)
    if cmd=="rock" and p=="scissor":
       print("User chose",cmd,"and computer chose",p)
       print("User win")
    if cmd=="paper" and p=="scissor":
       print("User chose",cmd,"and computer chose",p)
       print("User lose")
    if cmd=="scissor" and p=="rock":
       print("User chose",cmd,"and computer chose",p)
       print("User lose")
    if cmd=="rock" and p=="paper":
       print("User chose",cmd,"and computer chose",p)
       print("User lose")
    if cmd=="paper" and p=="rock":
       print("User chose",cmd,"and computer chose",p)
       print("User win")
    if cmd=="scissor" and p=="paper":
       print("User chose",cmd,"and computer chose",p)
       print("User win")
    elif cmd==p:
       print("User chose",cmd,"and computer chose",p)
       print("Tie")
    i = input("want to play again?")
    if i == "no" or i == "NO":
        break
