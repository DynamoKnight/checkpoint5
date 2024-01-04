# implement the Student class as per instructions
class Student:
    def __init__(self, student_number, file_name):
        self.student_number = student_number
        self.name = file_name
        if '/' in file_name:
            self.name = self.name[self.name.find('/') + 1 :len(self.name)]
        if '.' in self.name:
            self.name = self.name[0: self.name.find('.')]
        self.classes = {}
        with open (file_name) as file:
            for line in file.readlines():
                lst = line.split()
                self.classes[lst[0]] = int(lst[1])
            pass

    def __repr__(self):
        print(self.name, self.student_number, self.classes)

    def get_name(self):
        return self.name

    def get_student_number(self):
        return self.student_number

    def get_credits_for(self, class_name):
        if class_name not in self.classes:
            return None
        else:
            return self.classes[class_name]

    def get_classes(self):
        return list(self.classes.keys())