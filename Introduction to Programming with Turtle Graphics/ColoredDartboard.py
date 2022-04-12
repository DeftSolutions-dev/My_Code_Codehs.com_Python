radius=100
for i in range(4):
    penup()
    setposition(0,0)
    right(90)
    forward(radius)
    left(90)
    color_choice= input("What color to draw the circle?")
    color(color_choice)
    begin_fill()
    circle(radius)
    end_fill()
    radius=radius-25