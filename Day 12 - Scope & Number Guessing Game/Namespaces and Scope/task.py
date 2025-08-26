'''
def is_prime(num):
    while num != 2 and num != 3:
        if num == 1:
            return True
        elif (num%2) == 0 or (num%3) == 0:
            print(num)
            return True
        else:
            return False
    else:
        return False
print(is_prime(75))
'''

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")