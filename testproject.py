pupils = {"Alice":95,"Jason":30, "William":50, "Martin":100, "Dan":68}

for name, score in pupils:
    print("{name}, {score}")
    print("_" * 30)

total_score = 0
for score in pupils.values():
    total_score += score

class_average = total_score / len(pupils)

highest_score = max(pupils.values)
lowest_score = min(pupils.values)

print("Highest score :", highest_score)
print("Lowest score :", lowest_score)
print("-" * 30)

search_student = input("Enter a student's name to find their grade :")

student_grades = pupils.get(search_student)

if student_grades is not None:
    print("Student {search_student} received {student_grades}")
else:
    print('Student {search_student} is not here')
