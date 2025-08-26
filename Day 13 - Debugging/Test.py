'''number= int(input("Write number:"))
def odd_or_even(number):
    if number % 2 == 0:
        return print("This is an even number.")
    else:
        return print("This is an odd number.")
odd_or_even(number)'''

# exercise 1
'''
def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."
odd_or_even(4)'''

# exercise 2
'''
def is_leap(year):
    if year % 4 == 0:
        print(year % 4 == 0)
        print(year)
        if year % 100 == 0:
            print(year % 100 == 0)
            print(year)
            if year % 400 == 0:
                print(year % 400 == 0)
                print(year)
                print("1")
                return True
            else:
                print("2")
                return False
        else:
            print("3")
            return True
    else:
        print("4")
        return False
is_leap(2000)
'''

# exercise 3

def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
fizz_buzz(20)
