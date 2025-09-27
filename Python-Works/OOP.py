class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def introduce(self):
        print(f"Hi, I am {self.name}")


student = Student("Ayomide", 2435789)
student.introduce()


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Good day!! My name is {self.name}")


class Teacher(Person):
    
    def __init__(self, name, course):
        self.course = course


    def teach(self):
        print(f"I teach {self.course}")


t = Teacher("Amanda","Object Oriented Programming")
t.teach ()
        
