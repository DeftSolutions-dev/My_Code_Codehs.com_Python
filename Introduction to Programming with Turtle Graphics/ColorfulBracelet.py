speed(99)
def drawCircle():
    penup()
    forward(100)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    penup()
    backward(100)
    left(10)
for i in range(12):
    speed(99)
    color("blue")
    drawCircle()
    color("red")
    drawCircle()
    color("purple")
    drawCircle()
    speed(99)