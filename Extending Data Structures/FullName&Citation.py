name = input("First Name: ")
_name = input("Last Name: ")
print("Full name: "+str(name)+" "+str(_name))
name,_name = _name,name
print("Citation: "+str(name)+", "+str(_name))