try:
    age = int(input("How old are you?"))
except ValueError:
    print("You had inserted in wrong value.")
    age = int(input("How old are you?"))
if age > 18:
    print("You can drive at age {age}.")
