# This program computes the weighted grade point average for various students
# and displays which student has the highest GPA.
# Developer : Angela D. Tackett     CMIS102       20JUN2022

def main():

# Initialize------
    students = ["Anthony","John","Flea","Chad"] #RedHotChiliPeppers \m/
    

# Call------------    
    # Display Welcome Message
    Welcome()

    # Loop for each student
    for student in students:

        # Get grades and compute GPAs
        GPA = GetGrades(student)

        # Determine student with highest GPA
        largest = None
        if largest is None or GPA > largest:
            largest = GPA
        print('\n\n',student,'holds the overall highest GPA of',GPA,'!!!!!!')


# Functions----

def Welcome():
    print('\n\n(----------------Weighted GPA Calculator----------------)\n')
    print('  Follow the prompts to calculate GPAs and Top Student!\n\n')
    print('\t\tLEGEND:\n\t\t\t4 = A\n\t\t\t3 = B\n\t\t\t2 = C\n\t\t\t1 = D\n\t\t\t0 = F')


def GetGrades(student):
    GPA = 0
    # Display student name
    print("\n\nStudent: ",student)
     
    # Prompt for grades and validate [capitalization does not matter]
    # Discussion Grade (weighted = 20%)
    while 1:
        grade_1 = eval(input('Enter discussion grade [0-4]: '))
        if grade_1 == 0:
            grade_1 = 0 * .2
            break
        elif grade_1 == 1:
            grade_1 = .2
            break
        elif grade_1 == 2:
            grade_1 = 2 * .2
            break
        elif grade_1 == 3:
            grade_2 = 3 * .2
            break
        elif grade_1 == 4:
            grade_1 = 4 * .2
            break
        else:
            grade_1 = eval(input('Enter discussion grade [0-4]: '))
            

    # Quiz Grade (weighted = 30%)
    while 1:
        grade_2 = eval(input('Enter quiz grade [0-4]: '))
        if grade_2 == 0:
            grade_2 = 0 * .3
            break
        elif grade_2 == 1:
            grade_2 = .3
            break
        elif grade_2 == 2:
            grade_2 = 2 * .3
            break
        elif grade_2 == 3:
            grade_2 = 3 * .3
            break
        elif grade_2 == 4:
            grade_2 = 4 * .3
            break
        else:
            grade_2 = eval(input('Enter quiz grade [0-4]: '))
          
    # Program Assignment Grade (weighted 50%)
    while 1:
        grade_3 = eval(input('Enter programming assignment grade [0-4]: '))
        if grade_3 == 0:
            grade_3 = 0 * .5
            break
        elif grade_3 == 1:
            grade_3 = .5
            break
        elif grade_3 == 2:
            grade_3 = 2 * .5
            break
        elif grade_3 == 3:
            grade_3 = 3 * .5
            break
        elif grade_3 == 4:
            grade_3 = 4 * .5
            break
        else:
            grade_3 = eval(input('Enter programming assignment grade [0-4]: '))

    # Calculate overall GPA
    GPA = (grade_1 + grade_2 + grade_3)/3
    print('GPA: ',GPA)


    return GPA

#----EXECUTE--------------   
main()
        
