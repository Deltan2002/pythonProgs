months = ("january","february","march","april","may","june","july","august","sept","oct","november","december")
DOB = input("Enter your DOB in DD-MM-YYYY format\n")
index = int(DOB[3:5])-1
bd_month = months[index]
print("You were born in",bd_month)
