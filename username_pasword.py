user_name = input("please enter your username: ")
password = input("please enter pasword: ")
if user_name == "admin" and password == "admin":
    print("welcome")
elif user_name == 'admin' and password != "admin":
    print("wrong data!")
else:
    print(f'hello {user_name}')
    