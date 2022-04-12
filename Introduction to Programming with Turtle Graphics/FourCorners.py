speed(9)
square_length = int(input("What is the length of the square?"))
#---------------------------------------------------------------------#
def draw_square():
    for i in range(4):
        pendown()
        forward(square_length)
        left(90)
        penup()
#---------------------------------------------------------------------#
penup()
setposition(200 - square_length, -200)
draw_square()
#---------------------------------------------------------------------#
penup()
setposition(-200, 200 - square_length)
draw_square()
#---------------------------------------------------------------------#
penup()
setposition(200 - square_length, 200 - square_length)
draw_square()
#---------------------------------------------------------------------#
penup()
setposition(-200, -200)
draw_square()