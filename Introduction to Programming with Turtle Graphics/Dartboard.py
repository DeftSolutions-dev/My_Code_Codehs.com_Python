speed(0)
radius = 25
penup()
setposition(0,-25)

def drawCircles():
    pendown()
    circle(radius)
    right(90)
    penup()
    forward(25)
    pendown()
    left(90)

for i in range(4):
    drawCircles()
    radius = radius + 25