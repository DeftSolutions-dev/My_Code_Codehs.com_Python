"""In this code, Tracy builds a pyramid"""
penup()
setposition(-100,-200)
for i in range (3):
    pendown()
    circle(50)
    penup()
    forward(100)
setposition(-50,-115)
#Now Tracy will draw a circle
for i in range (2):
    pendown()
    circle(50)
    penup()
    forward(100)
setposition(0,-30)
for i in range (1):
    pendown()
    circle(50)
    penup()
#Now Tracy will take a break