def count_letter (string):
    # initialize counters for uppercase and lowercase
    upper_counter = 0
    lower_counter = 0
    for char in string:
        if 64<ord(char)<91:
            # check if character is uppercase (A-Z)
            upper_counter += 1
        elif 96<ord(char)<123:
             # check if character is lowercase (a-z)
            lower_counter += 1
    return(upper_counter , lower_counter)

def prime_num():
    number = int(input("enter the number: "))
    is_prime = True
    while number<=1:
        print(" enter a number greater than 1. 0 and 1 are not prime numbers!")
        number = int(input("enter the number: "))
    for num in range(2 , number-1):
        if number % num == 0:
            is_prime = False
            break
    if is_prime:
        print("its a prime number.")
    else:
        print("its not a prime number.")        


def check_string(string):
    if len(string) == 0:
        return None
    elif string[0] == string[-1]:
        return True
    else:
        return False


def show_employee(name,salary = 9000):
    print(f'name: {name},salary: {salary}')


def factoriel(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    print(result)


factoriel(10)