speed(99)
def set_position(x,y):
    penup()
    setposition(x,y)
    pendown()

#diamond
set_position(-100,70)
begin_fill()
color("red")
circle(60,360,4)
end_fill()
#circle
set_position(100,70)
begin_fill()
color("blue")
circle(60)
end_fill()
#pentagon
set_position(100,-150)
begin_fill()
color("green")
circle(60,360,5)
end_fill()
#half cirlce
set_position(-130,-150)
begin_fill()
color("yellow")
circle(60,180)
end_fill()