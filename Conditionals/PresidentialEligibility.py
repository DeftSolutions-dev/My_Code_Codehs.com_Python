age = int(input("Age: "))
born = str(input("Born in the U.S.?(Yes/No): "))
year = int(input("Years of Residency: "))
if age>=35 and born=="Yes" and year>=14:
    print("You are eligible to run for president...")
else:
    print("You are not eligible to run for president...")