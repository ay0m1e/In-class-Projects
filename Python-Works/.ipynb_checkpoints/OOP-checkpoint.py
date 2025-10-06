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
        
def fizzBuzz(n):
    # Write your code here
    for i in range (1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

n = 15

fizzBuzz(n)