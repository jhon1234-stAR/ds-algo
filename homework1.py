class Student:
    # constructor
    def __init__(self, name, age, grade, attendance):
        self.name = name
        self.age = age
        self.grade = grade
        self.attendance = attendance

    # getter method
    def get_name(self):
        return self.name

    # setter method
    def set_grade(self, new_grade):
        self.grade = new_grade
        return self.grade

    # custom method
    def increase_attendance(self):
        self.attendance = self.attendance + 1

    # display student information
    def showStudent(self):
        print(
            "Hello, I am a student named {}, age {}, grade {}, attendance {}"
            .format(self.name, self.age, self.grade, self.attendance)
        )

# object
student1 = Student("Alice", 16, "10th Grade", 20)

print(student1.get_name())

print(student1.set_grade("year 11"))

student1.increase_attendance()

student1.showStudent()
