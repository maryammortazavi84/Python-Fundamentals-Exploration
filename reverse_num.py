number = int(input("please enter a number: "))
reversed_num = 0
while number :
    reversed_num = reversed_num*10 + (number%10)
    number = number//10
print(reversed_num)