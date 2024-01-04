# implement code as per instructions
from student import Student
def main():
    std_1 = Student(1551515, 'pablo.txt')
    std_2 = Student(1231231, 'arlo.txt')
    print(std_1.get_name(), std_1.get_student_number(), std_1.get_credits_for('CSE163'))
    print(std_2.get_name(), std_2.get_student_number(), std_2.get_credits_for('CSE163'))

if __name__ == '__main__':
    main()