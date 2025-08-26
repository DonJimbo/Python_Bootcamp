from ctypes import c_int16


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

a= add(4, 2)
b= subtract(2, 3)
c= multiply(4, 8)
d= divide(6, 7)

dictionary1 = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

dictionary2 = {
    '+': a,
    '-': b,
    '*': c,
    '/': d
}



print("------------------------------------------------------------------------------------"*2)
from art import logo
print(logo)

for maths in dictionary1:
    c1 = float(input("Please, type your first number:"))
    for symbol in dictionary1:
        print(symbol)
    c2 = input("Please, type your mathematical operator:")
    c3 = float(input("Please, type your second number:"))
    result = dictionary1 [c2](c1,c3)
    print(f"Result: {result}")

    c4 = input(f"Do you want to continue? Current count is: {result} ")
    while c4 == "yes":
        c2 = input("Please, type your mathematical operator:")
        c3 = int(input("Please, type your second number:"))
        result2 = dictionary1 [c2](result,c3)
        result = result2
        print(f"Result: {result}")
        c4 = input("Do you want to continue?")
        if c4 == "no":
            dictionary1[c2](c1, c3)
    if c4 == "no":
        dictionary1[c2](c1, c3)

