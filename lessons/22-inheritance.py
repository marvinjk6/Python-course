'''
Inheritance - inherits very single thing which we have in the class 
we're going to import the attributes from student.py file, that has the class Student

'''

from student import Student

class Person(Student):
    pass # to avoid any error

p1 = Person()
print(p1.name)
print(p1.age)
