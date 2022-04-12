age = int(input("Age: "))
born = str(input("Born in the U.S.?(Yes/No): "))
year = int(input("Year of Residency: "))
if ((age>=35)and(born=="Yes")and(year>=14)):
    print("You are eligible to run for president!")
else:
    print("You are not eligible to run for president.")
if age<35:
    print("You are to young. You must be at least 35 years old.")
if born=="No":
    print("You must be born in the U.S. to run for president.")
if year<14:
    print("You have not been a resident for long enough.")