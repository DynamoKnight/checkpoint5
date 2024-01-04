from run_dog_tests import main as test_dogs
from run_ed_tests import main as test_ed
from run_pair_tests import main as test_pair
from run_student_tests import main as test_student

def main():
    test_dogs()
    test_ed()
    test_pair()
    test_student()

if __name__ == '__main__':
    main()