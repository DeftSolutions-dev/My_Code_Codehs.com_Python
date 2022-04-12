my_float = 3.3312
while True:
    guess = float(input("My number: "))
    my_float=round(my_float,2)
    guess=round(guess,2)
    if guess==my_float:
        print("Correct!")
        break
    elif guess>my_float:
        print("Too high!")
    else:
        print("Too low!")