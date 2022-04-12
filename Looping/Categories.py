for i in range(3):
    category=input("Enter a category: ")
    name=""
    for j in range(3):
        name += input("Enter something in that category: ")
    print(category+": "+name)