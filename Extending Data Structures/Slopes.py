list=[]
for i in range(5):
    x =int(input("X: "))
    y =int(input("Y: "))
    list.append((x,y))
for j in range(4):
    y1=list[j][1]
    x1=list[j][0]
    y2=list[j+1][1]
    x2=list[j+1][0]
    slope = (y2-y1)/(x2-x1)
    print("Slope " + str(list[j])+ " and "+str(list[j+1]) +": "+str(slope))