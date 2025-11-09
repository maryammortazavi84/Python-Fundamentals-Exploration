"""
this program prints this pattern
11111111
2222222
333333
44444
5555
666
77
8
"""




n = 8
for i in range(1, n+1): #Outer loop → goes from 1 up to n
    for x in range(i , n+ 1):#Inner loop → repeats (n - i + 1) times
        print(i, end=" ")
    print()
