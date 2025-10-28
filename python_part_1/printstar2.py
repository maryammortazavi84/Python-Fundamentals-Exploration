"""
This program draws an n x n square pattern of stars (*).
The borders (first/last row, first/last column) 
and both diagonals are filled with stars, 
while the other positions remain empty (spaces).
"""



n = int(input("enter a number: "))
for row in range(1, n+1):
    for column in range(1, n+1):
          # Print stars on borders or diagonals
        if row == 1 or row == n or column == 1 or column == n or row == column or row + column == n+1:
            print(end= "*")
        else:
            print(end= " ")
    print()