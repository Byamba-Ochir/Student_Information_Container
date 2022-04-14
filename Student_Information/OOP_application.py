from datetime import date
from datetime import datetime

class Person:
    organization= "ASU"

    def __init__(self,name,dob,age):
        self.name= name
        self.dob = dob
        self.age = age

    def __repr__(self):
        return f"Name:{self.name}, Date of Birth:{self.dob}, Age:{self.age}, "


class Student(Person): 

    def __init__(self, name, dob, age, grade, subjects):
        super().__init__(name, dob, age)
        self.grade = grade
        self.subjects = subjects

    def __repr__(self):
        return super().__repr__() + f"Grade:{self.grade}, Subjects:{self.subjects}"

# This function validates the date of birth input
def get_dob():

    dob = input("Date of Birth (yyyy/mm/dd): ")
    try:
        year,month,day = dob.split("/")

        test_str = f"{year}/{month}/{day}"
        format = "%Y/%m/%d"

        if(not datetime.strptime(test_str, format)):
            print("That is not a valid date buddy. Try Again")
            return get_dob()

        else:
            return year,month,day

    except ValueError:

        # To make the code indentify the input that are also separated by (" "/space)
        try:
            year,month,day = dob.split(" ")

            # Testing the date if its valid or not
            test_str = f"{year}/{month}/{day}"
            format = "%Y/%m/%d"

            if(not datetime.strptime(test_str, format)):
                print("That is not a valid date buddy. Try Again")
                return get_dob()

            else:
                return year,month,day

        except ValueError:
            print("Invalid input, please try again!")
            return get_dob()
        

def get_Grade():

    grades = ('1','2','3','4','5','6','7','8','9','10','11','12')

    grade = input("Grade: ")

    if (not grade in grades):
        print("Invalid Input. Try Again.")
        return get_Grade()

    else:
        return grade


picked_subjects = []
# Function that lets the students select multiple subjects they attend to
def select_Subjects():

    # Makes the code only accept integer numbers.
    try:
        index = int(input("Enter the number beside the subject you take >> "))

        # Checks if the chosen number is in the list of subjects.
        if(index in possible_indexes):

            # Accepts the input and prints that the subject is added.
            picked_subjects.append(all_subjects[index-1])
            print(f"{all_subjects[index-1]} added!")

            # For choosing multiple subjects
            def Confirm():

                confirm = input("Do you want to add more subjects? (y/n) ")
                if(confirm.lower() == "y" or confirm.lower() == "yes"):
                    return select_Subjects()

                # Ends the function and returns all the subjects the student chose
                elif(confirm.lower() == "n" or confirm.lower() == "no"):
                    return picked_subjects

                else:
                    print("Invalid Input.")
                    return Confirm()

            Confirm()

            return picked_subjects

        # If the input is integer but not in the list
        else:
            print(f"Select number between 1 and {len(all_subjects)}!")
            return select_Subjects()

    # If the input is not an integer
    except ValueError:
        print("Invalid input. Try again.")
        return select_Subjects()


def get_Subjects():

    print("Please select your subjects from below:")
 

    # Shows all the available subjects to choose from
    for i in range(len(all_subjects)):
        print(f"{i+1}. {all_subjects[i]}")

    # Lets the user choose subjects

    picked_subjects = []
    picked_subjects = select_Subjects()

    return picked_subjects


def Calculate_Age(y,m,d):

    today = date.today()
    age = today.year - y - ((today.month, today.day) < (m, d))

    return age


#main program
students = []
all_subjects = sorted(["English language arts","PreCalculus","AP Calculus","Physics","Chemistry","Physical Education","Art","Band", "Chinese", "French", "US History","Biology","Computer Science"])

possible_indexes = []
# Creates a list that contains from 1 to length of all the subjects.
for i in range(len(all_subjects)):
    possible_indexes.append(int(i+1))

print("Welcome to ASU Student Services")

while True:

    name = input("Name:")
    dob_year,dob_month,dob_day = get_dob()
    age = Calculate_Age(int(dob_year),int(dob_month),int(dob_day))
    grade = get_Grade()
    subjects = []
    subjects = get_Subjects()
    picked_subjects = []
    

    dob = (f'{dob_year}',f'{dob_month}',f'{dob_day}')
    students.append(Student(name,dob,age,grade,subjects))
    answer = None
    while answer not in ('y','n'):
        answer = (input("Would you like to enter another student (y/n)")).lower()

    if answer == 'n':
        print("You have entered the following students")
        print("----------------------------------------")
        for student in students:
            #prints the students
            print(student)
        break


# Creates and saves the students information in the text.txt file
with open("text.txt",'w', encoding = 'utf-8') as f:
    for student in students:
        f.write(f"{str(student)}\n")