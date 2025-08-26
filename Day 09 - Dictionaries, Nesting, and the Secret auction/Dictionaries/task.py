
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}
for key in student_scores:
    student_grades[key] = student_scores[key]
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81 <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71 <= 80:
        student_grades[key] = "Acceptable"
    elif student_scores[key] <= 70:
        student_grades[key] = "Fail"
print(student_grades)


