#n = 5
#for i in range(n):
#    for j in range(n - i):
#        print("*" , end= "")
#    print(i * 2 * " ", end= "")
#    for k in range(n - i):
#        print("*" , end= "")
#    print()
#for a in range(1 , n):
#    for b in range(0 ,a+1):
#        print("*" , end= "")
#   print((n-a-1)*2* " " , end= "")
#   for c in range(0 ,a+1):
#       print("*" , end= "")
#   print()


n = 5
for i in range(n):
    a = n-i
    print( a * "*" + 2 * i * " " + a * "*"  )
for j in range (1 , n +1):
    print( j * "*" + 2 * (n-j) * " " + j * "*" )