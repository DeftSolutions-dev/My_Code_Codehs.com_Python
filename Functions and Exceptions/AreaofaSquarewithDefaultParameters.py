side_length = 0
def calculate_area(side_length = 10):
    print("The area of a square with sides of length "+
    str(side_length)+
    " is "+
    str(side_length**2)+
    ".")
side_length = int(input("Enter side length: "))
if side_length <= 0:
    side_length = 10
calculate_area(side_length)