magic_number = 3
while True:
    guess = int(input("Guess my number: "))
    if guess == magic_number:
        print("Correct!")
        break
    print("Too high!")