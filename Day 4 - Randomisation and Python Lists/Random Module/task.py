import random
from dis import code_info

#import my_module
#print(my_module.my_favorite_number)

#random_integer = random.randint(1,10)
#print(random_integer)

#random_number_0_to_1 = random.random ()
#0.0 <= random.random() < 1.0
#print(random_number_0_to_1)

#random_floating = random.uniform(1,10)
#print(random_floating)

Coin_flip = random.randint(0,1)
if Coin_flip == 0:
    print("Head")
elif Coin_flip == 1:
    print("Tail")
