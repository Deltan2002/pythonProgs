f1 = 0
f2 = 1
n = int(input("Enter the number of terms: "))
if n == 1:
    print(f1)
elif n == 2:
    print(f1+f2, end=" ")
else:
    print(f1, f2, end=" ")
    for i in range(2, n):
        f3 = f1 + f2
        print(f3, end=" ")
        f1 = f2
        f2 = f3
