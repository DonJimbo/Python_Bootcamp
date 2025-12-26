import  pandas

student_dict = {
    "student": ["Angela", "Rob", "Pepe"],
    "score": [21, 14, 64]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

'''Loop through row of a data frame '''
for (index, row) in student_data_frame.iterrows():
    print(row.score)

score = {row.score for (index, row) in student_data_frame.iterrows()}
print(score)


'''Loop through row of a data frame with IF'''
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

score = {row.score for (index, row) in student_data_frame.iterrows() if row.student == "Angela"}
print(score)