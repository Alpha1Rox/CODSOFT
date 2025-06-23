contact={}
def add_contact():
    for x in iter(int, 1):
        name = input("Enter the name")
        phnumber = input("Enter the phone number")
        email = input("Enter the email")
        address = input("Enter the address")
        contact[name]={"name":name,"phnumber":phnumber,"email":email,"address":address}
        print("Contact is added")
        e =input("Want to stop:(yes or no)")
        if e=="yes":
            break
def view_contact():
    print(contact)
def search_contact(query):
 for name, keyval in contact.items():
    if query in name or query in keyval["phnumber"]:
         print(contact[name]["name"],end=',')
         print(contact[name]["phnumber"], end=',')
         print(contact[name]["email"],end=',')
         print(contact[name]["address"],end=',')
def update_contact(name,phnumber=None,email=None,address=None):
    if name in contact:
        if email is not None:
            contact[name]["email"] = email
        elif phnumber is not None:
            contact[name]["phnumber"] = phnumber
        elif address is not None:
            contact[name]["address"] = address
def delete_contact(name):
    contact.pop(name)
def main():
    for x in iter(int, 1):
      cmd = int(input("Enter the choice:"))
      if cmd==1:
         add_contact()
      elif cmd==2:
          if len(contact)==0:
              print( "No contact")
          elif len(contact) != 0:
               view_contact()
      elif cmd==4:
        a=input("Enter the parameter to change")
        b=input("Enter the value of parameter")
        c=input("Enter the name of the person")
        if a=="email":
          update_contact(c,email=b)
        if a=="phnumber":
          update_contact(c,phnumber=b)
        if a=="address":
          update_contact(c,address=b)
      elif cmd==3:
        q=input("Enter the name or phone number for search")
        search_contact(q)
      elif cmd==5:
        a=input("Enter the name to delete")
        delete_contact(a)
      i=input("want to perform more function(yes or no)")
      if i=="no":
          break
if __name__ == "__main__":
    main()


