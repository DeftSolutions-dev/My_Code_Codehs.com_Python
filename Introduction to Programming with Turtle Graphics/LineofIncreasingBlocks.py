speed(0)
penup()
setposition(-150, 0)
length = 10
length0 = 3
def square():
    for i in range(4):
        pendown()
        forward(length)
        left(90)
        penup()  

for i in range(5):
    square()
    length = length + 10
    length0 = length0 + 10
    forward(length0 *2)