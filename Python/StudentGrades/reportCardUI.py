import student

def showStudent(aStudent):
    print('')
    print('Student Name: ' + aStudent.name)
    for category in aStudent.categories:
        print('Category: ' + category.name + ' has Weight: ' + str(category.weight))


studentName = raw_input("Enter the Student's Name: ")
theStudent = student.Student(studentName)

print('')
keepGoing = True;
while keepGoing:
    categoryName = raw_input("Please Enter a grade catgeory (DONE): ")
    if (categoryName.lower() == 'done'):
        keepGoing = False
    else:
        theStudent.addCategory(categoryName)

while not theStudent.categoriesAreValid():
    print('')
    print('Enter weights for categories (must add to 100%)')
    for category in theStudent.categories:
        percentage = raw_input('Please enter the % weight for ' + category.name + ': ')
        category.setWeight(percentage)

keepGoing = True
while keepGoing:
    print('')
    for index, category in enumerate(theStudent.categories):
        print(str(index + 1) + '. Enter: ' + category.name)
    print('R. See the Report Card')
    print('Q. Quit')
    option = raw_input('Choose an Option: ')
    if option.lower() == 'q':
        keepGoing = False
    #else:
        # DO the option


showStudent(theStudent)
