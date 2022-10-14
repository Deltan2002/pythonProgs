print("PROGRAM TO FIND AREA AND CIRCUMFERENCE OF THE CIRCLE\n")
import math
r = float(input("Enter the radius of a circle\n"))
Area = math.pi*r**2
Circumference = 2*math.pi*r
print("The area is: ",round(Area,4),"\nThe circumference is: ",round(Circumference,4))
