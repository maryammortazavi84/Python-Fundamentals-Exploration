row = 10
for i in range(row//2,row,2):
    for j in range(1,row-i,2):
        print(end=" ")
    for j in range(1,i+1):
        print(end="*")
    for j in range(1,row-i):
        print(end=" ")
    for j in range(1,i+1):
        print(end="*")

    print()

for r in range(2*row):
    for b in range(2*(row-1),1):
        print(end="*")
        row-=1
    print()