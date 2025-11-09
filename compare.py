"""
if the price is higher will the quality increase?
"""
found = False
laptop_list = [(1, 5), (5, 6), (7, 9), (20, 30)]

laptop_list = sorted(laptop_list)# Sort by price
for i in range(len(laptop_list)-1):
    current = laptop_list[i]
    next_one = laptop_list[i+1]
    if current[1] >= next_one[1]:# Check if current quality >= next quality
        found = True
        print('found')
        break


if not found:
    print("not found")        

