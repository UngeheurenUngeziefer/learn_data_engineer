# multiple classes

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max = max_students
        # method didn't assigned
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        summ_of_grades = 0
        for student in self.students:
            summ_of_grades += student.get_grade()

        return summ_of_grades / len(self.students)

s1 = Student('Tim', 19, 95)
s2 = Student('Bill', 19, 75)
s3 = Student('Jill', 19, 65)

course = Course('Science', 2)
course.add_student(s1)
course.add_student(s2)
print(course.students)
print(course.get_average_grade())
