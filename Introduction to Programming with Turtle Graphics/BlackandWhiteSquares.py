speed(10)
penup()
setposition(-100,0)
count=0
def makeS(num):
    if num % 2==0:
        begin_fill()
    for i in range(4):
        forward(25)
        left(90)
    end_fill()
    penup()
    pendown()
for i in range(6):
    pendown()
    makeS(i)
    penup()
    forward(35)