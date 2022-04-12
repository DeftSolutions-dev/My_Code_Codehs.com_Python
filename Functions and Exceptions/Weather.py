def _sunny():
    print("On a sunny day, sandals are appropriate footwear!")
def _rainy():
    print("On a rainy day, galoshes are appropriate footwear!")
def _snowy():
    print("On a snowy day, boots are appropriate footwear!")

guess_weather = input("What the weather like? (sunny, rainy, snowy): ")
if guess_weather == "sunny":
    _sunny()
elif guess_weather =="rainy":
    _rainy()
elif guess_weather =="snowy":
    _snowy()
else:
    print("Error!")