import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student: students_scores[student] for student in students_scores if students_scores[student] >= 60}
print(passed_students)