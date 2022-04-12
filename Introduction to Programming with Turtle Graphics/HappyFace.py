speed(10)
penup()
def drawCircle(radius,colorC):
    pendown()
    color(colorC)
    begin_fill()
    circle(radius)
    end_fill()
    penup()
setposition(0,-100)
drawCircle(100,'yellow')
setposition(30,30)
drawCircle(10,'black')
setposition(-30,30)
drawCircle(10,'black')
happy = input("How do you feel?: ")
    
    
if happy == "happy":
    setposition(-60,0)
    pendown()
    right(90)
    pensize(9)
    circle(60,180)