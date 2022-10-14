print("BODY MASS INDEX")
height=float(input("Enter your height in meters\n"))
weight=float(input("Enter your weight in kgs\n"))

bmi=weight/(height*height)

print("THE BMI(BODY MASS INDEX) IS: ",round(bmi,2))

if(bmi<=18.5):
   print("You are UNDERWEIGHT\n")
elif(bmi>18.5 and bmi<=24.9):
     print("You are NORMAL WEIGHT\n")
elif(bmi>24.9 and  bmi<=29.9):
     print("You are OVERWEIGHTED\n")
else:
     print("You have OBESITY, since your BMI is above the normal level i.e, 30")
