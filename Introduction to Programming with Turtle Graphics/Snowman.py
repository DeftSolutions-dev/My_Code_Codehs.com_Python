speed(0)
penup()
setposition(0,-200)
def drawCircle(radius):
    color("grey")
    pendown()
    begin_fill()
    circle(radius)
    end_fill()
    penup()
    left(90)
    forward(radius*2)
    right(90)

_radius = int(input("What is the size?:  "))
drawCircle(_radius)
drawCircle(_radius / 2)
drawCircle(_radius / 4)