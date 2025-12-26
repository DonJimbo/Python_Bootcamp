
''' List comprehension '''
# Numbers
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]

'''
numbers = [1, 2, 3]
new_numbers = []
for n in numbers:
    add_1 = n + 1
    new_numbers.append(add_1)
print(new_numbers)
'''

# Strings
name = "Jaime"
letters_list = [letter for letter in name]

'''
name = "Jaime"
letters_list = []
for l in name:
    letters_list.append(l)
print(letters_list)
'''

# Ranges
range = range(1, 5)
new_range = [number * 2 for number in range]
print(new_range)

'''
range = range(1, 5)
new_range = []
for item in range:
    double_values = item * 2
    new_range.append(double_values)
print(new_range)
'''

''' Conditional List comprehension '''
names = ["Pepe", "Joaquin", "Josefina", "Ana", "Jaime"]
new_list = [name.upper() for name in names if len(name) > 5]

# or "in" in "if"
with open("file1.txt") as file1:
    contents1 = file1.readlines()
with open("file2.txt") as file2:
    contents2 = file2.readlines()

result = [int(num) for num in contents1 if num in contents2]
print(result)

'''
names = ["Pepe", "Joaquin", "Josefina", "Ana", "Jaime"]
new_range = []
for name in names:
    if len(name) > 5:
        new_range.append(name)
print(new_range)
'''