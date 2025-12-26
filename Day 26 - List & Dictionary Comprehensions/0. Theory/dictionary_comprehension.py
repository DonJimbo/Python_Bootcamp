import random

'''Generate new dictionaries'''
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

names = ["Javi", "Guillem", "Oscar", "Jimbo", "Noah", "El cicatrices"]
student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)

'''Generate new dictionaries with IF'''
# Same as:
# student_pass = [name for name, score in student_scores.items() if score> 60]

student_pass = {name:score for (name,score) in student_scores.items() if score > 60}
print(student_pass)

