"""
Commands

w = to replace
a = to add
r = to read
"""

"""
Option 3  --> Create new text in file
"""
with open("my_file.txt", mode="w") as file:
    file.write("\nNew text.")

"""
Option 2 -->
"""
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

""" 
Option 1 -->
"""
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()
