speed(0)
penup()
setposition(-150,0)

def drawCircle(color_choice): 
    color(color_choice)
    begin_fill()
    circle(20)
    end_fill()
    forward(35) 

for i in range(2):
    drawCircle("blue")
    drawCircle("green")
    drawCircle("yellow")
    drawCircle("red")