"""
This program generates all 4-digit numbers using the digits 5, 6, 7, and 8
without repeating any digit, and prints them in descending order.
"""

numbers = []
digits = [5 , 6 , 7 ,8]
for a in digits:                  ## Generate all 4-digit numbers without repeating digits
    for b in digits:
        if b != a:
            for c in digits:
                if c != a and c !=b:
                    for d in digits:
                        if d != a and d != b and d != c:
                            number = (a * 1000) + (b * 100) + (c * 10) + d
                            numbers.append(number)

numbers.sort(reverse= True)
for num in numbers:
    print(num)



"""
for a in range(8 , 4  , -1):
    for b in range(8 , 4 , -1):
        for c in range (8 , 4 , -1):
            for d in range(8 , 4 , -1):
                if (a == b) or (a == c) or (a == d) or (b == c) or (b == d) or (c == d):
                    continue
                print((a * 1000) + (b * 100) + (c * 10) + d)
"""