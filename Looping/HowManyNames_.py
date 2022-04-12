my_string = int(input("How many names you have "))
names = ""
for i in range(my_string):
    my_string = input("Enter a name: ")
    names += str(my_string)+" "
print(names)