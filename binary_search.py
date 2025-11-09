"""
    Recursive binary search function.
    Returns the index of target or -1 if not found.
"""

search = input("enter the number list with the number you want to find in the beginning: ")
number_list = [] 
search = search.split(",")
for char in search:
    try:
        number_list.append(int(char))
    except ValueError:
        pass

target = number_list[0]
del number_list[0]
left = 0
right =len(number_list) -1

def binary_search(number_list:list, target:int, left:int, right:int):
    if left>right :
        return -1
    mid = (left + right) // 2
    if number_list[mid] == target:
        return mid
    elif number_list[mid] < target:
        return binary_search(number_list, target, mid+1, right)
    else:
        return binary_search(number_list, target, left, mid-1)
    
answer = binary_search(number_list, target, left, right)
print(answer)

