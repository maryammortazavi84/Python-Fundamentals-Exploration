"""
Sums the digits of a number repeatedly until one digit remains
"""

#functions
def equasion(number:str) -> int:
    result = 0
    for digit in number:
        digit = int(digit)
        result += digit
    return result
#main code
number = (input("number? "))
result = equasion(number)
while result>10 :
    number = str(result)
    result = equasion(number)
print(result)

