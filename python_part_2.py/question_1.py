n = 5
for i in range(1,n+1):
    if i == 1:
        print("*")

    print("*", end="")
    for j in range(1,i+1):
        print(j, end="")
    for m in range(i-1,0,-1):
        print(m, end="")
    print("*", end="")
    print()

for a in range(n-1,0,-1):
    print("*", end="")
    for b in range(1,a+1):
        print(b, end="")
    for c in range(a-1,0,-1):
        print(c, end="")
    print("*", end="")
    print() 

    if a == 1:
        print("*")
 