"""
this is an ordering program you can only order from the menu
"""
menu = ["pizza", "mushroom", "number 47", " number 9 large", "number 6 with extra dip"]
order_list = []
print(menu)

order = input("please enter your order: ").lower().strip()
order=order.split()
for item in order:
    if item in menu:
        order_list.append(item)
    else:
        print("this item is not on menu")
print(f'this is your order:{order_list}')