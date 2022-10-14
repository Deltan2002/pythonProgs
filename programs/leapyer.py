  year = int(input("enter the year\n"))
   if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        print("LEAP YEAR")
    else:
        print("not a leap year")


# a = int(input("enter the number a\n"))
# b = int(input("enter the number b\n"))
# for i in range(a, b+1):
#     c = i**2
#     if c <= b:
#         print(c)
