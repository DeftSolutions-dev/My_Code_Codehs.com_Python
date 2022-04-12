_dict ={}
while True:
    name = input("Name: ")
    name.lower()
    if name=="":
        break
    elif name in _dict:
        print("Phone number: "+ str(_dict[name]))
    else:
        phone = input("Enter phone number: ")
        _dict[name]=phone
print(_dict)