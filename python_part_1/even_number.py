even_numbers = []
while(True):
    input_string = input("please enter 10 numbers with one space in between each: ")
    numbers = input_string.split()
    if len(numbers) != 10:
        print("enter exactly 10 numbers.")
        continue
    if not all(number.isdigit() for number in numbers):
        print("only positive numbers are accepted.")
        continue
    numbers = [int(number) for number in numbers]
    break
for num in numbers:
    if num %2 == 0:
        even_numbers.append(num)

print(f' even numbers in this list: {even_numbers}')
"check"