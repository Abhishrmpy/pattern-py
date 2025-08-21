
# n = int(input("Enter the numer of row:"))
# for i in range(1, n + 1):
#     print(" " * (n-i) + "*" * i)


#now how to print with nested loop 


# n = int(input("Enter the number of rows: "))

# for i in range(1 , n + 1):
#     for j in range(n - 1):
#         print(" " , end="")
#     for j in range(i):
#         print("*", end= "")
#     print()

n = int(input("Enter rows: "))

for i in range(1, n + 1):                # outer loop = rows
    for j in range(n - i):               # spaces first
        print(" ", end="")
    for j in range(i):                   # then stars
        print("*", end="")
    print()                              # move to new line
