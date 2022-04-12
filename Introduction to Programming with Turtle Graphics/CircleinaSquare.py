speed(0)
radius = int(input("What is the size?:  "))
x=0
y=0
penup()
setposition(x-radius, y-radius)
pendown()

def drawSquare(radius):
    color("red")
    begin_fill()
    for i in range(4):
        forward(radius*2)
        left(90)
    end_fill()

def drawCircle(radius):
    pendown()
    setposition(0, y-radius)
    penup()
    color("blue")
    begin_fill()
    circle(radius)
    end_fill()

drawSquare(radius)
drawCircle(radius)