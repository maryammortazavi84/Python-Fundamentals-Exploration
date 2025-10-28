my_list = []
counter = 1
while True :
    item =input(f"please enter item {counter}:")
    if item in my_list:
        print('you already have that on your list')
    else:
        counter = counter +1
        my_list.append(item)
    if len(my_list) == 5:
        my_list = sorted(my_list)
        print(f'this is your list: {my_list}')
        break
  
    