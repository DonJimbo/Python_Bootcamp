
'''args'''


def add(*args):
    sum = 0
    # Positional argument
    print(args[1])

    # Loop
    for n in args:
        sum += n
    return sum

print(add(1,2,3,4,5,6,7,8,9))

'''kwargs'''

def calculate (n, **kwargs):
    print(type(kwargs))
    n *= kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


# Option 1 - To extract the dictionary items
    # def calculate (n, **kwargs):
    #    for key,value in kwargs.items():
    #        print(key)
    #        print(value)
    # calculate(add=3, multiply=5)

# Option 2 -To extract the dictionary items
        # print(kwargs["add"])

class Car:
    def __init__(self,**kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("coloe")
        self.seats = kwargs.get("seats")

my_car = Car(make="Nissan",model="GT-R")
print(my_car.model)

