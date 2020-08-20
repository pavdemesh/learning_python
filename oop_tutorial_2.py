# https://www.youtube.com/watch?v=JeznW_7DlB0

class Student:
    def __init__(self, name, age, grade):
        self.st_name = name
        self.st_age = age
        self.st_grade = grade

    def get_grade(self):
        return self.st_grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students_list = []

    def add_student(self, student_object):
        if len(self.students_list) < self.max_students:
            self.students_list.append(student_object)
            return True
        return False

    def get_average_grade(self):
        average_grade = 0
        for student_object in self.students_list:
            average_grade = average_grade + student_object.get_grade()
        return average_grade / float(len(self.students_list))


s1 = Student("Mike", 23, 43)
s2 = Student("Alexander", 18, 98)
s3 = Student("Xena", 22, 87)

course1 = Course("Biology", 2)
course2 = Course("Accounting", 5)

course1.add_student(s1)
course1.add_student(s2)

print(course1.students_list[0].st_grade)

print(course1.get_average_grade())
# print(course1.add_student(s3))
# print(course1.students_list)
