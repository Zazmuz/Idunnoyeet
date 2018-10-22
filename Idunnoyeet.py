import random

student = input('Input the students name: ')
grading = None
graded = None
upperclasskid_grading = None
bad_stuff_cuz_i_cant_do_python = 0
times = 0
grades = ["F", "B", "C", "D", "E"]
upperclasskid_grades = ["A", "B", "MVG", "PERFECT"]
for grade in grades:
    grading = random.randint(0, 4)
    for names in ["rasmus", "matilda", "sofia", "blenda", "ranja"]:
        if bad_stuff_cuz_i_cant_do_python == True:
            break
        if student.lower() == names:
            upperclasskid_grading = random.randint(0, 3)
            print(student + "'s grade is: " + upperclasskid_grades[upperclasskid_grading])
            bad_stuff_cuz_i_cant_do_python = 1
        else:
            if bad_stuff_cuz_i_cant_do_python == True:
                break
            print (student + "'s grade is: " + grades[grading])
            bad_stuff_cuz_i_cant_do_python = 1
            print (grading)

