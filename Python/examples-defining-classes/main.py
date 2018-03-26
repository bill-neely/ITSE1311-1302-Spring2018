# create 3 instances of Student class, with different names
# create 2 instances of Course, wioth different names and assign students
import student

students = []
students.append(student.Student('Bill'))
students.append(student.Student('Bob'))
students.append(student.Student('Jenny'))

students[0].recordGrade(100)
students[1].recordGrade(75)
students[2].recordGrade(92)

students[0].recordGrade(95)
students[1].recordGrade(50)
students[2].recordGrade(93)

for student in students:
    print('Student: ' + student.firstName + ' has ' + str(len(student.grades)) + ' grades, with an average of ' + str(student.average()))
