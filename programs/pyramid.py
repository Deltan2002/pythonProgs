
# n = int(input("Enter the row : "))
# for i in range(n):
#     for j in range(i+1):
#         print(j+1, end=" ")
#     print()

# a = 1
# n = int(input("Enter the row : "))
# for i in range(n):
#     for j in range(i+1):
#         print(a, end=" ")
#         a += 1
#     print()

# n = int(input("Enter the rows: "))

# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         print(j, end=" ")

#     print()

n = int(input("Enter the rows: "))

for i in range(n, 0, -1):
    c = 'a'
    for j in range(1, i+1):
        print(c, end=" ")
        c = chr(ord(c)+1)
    print()
