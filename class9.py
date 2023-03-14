"""
We will use this module to show inheritance
"""

class Person:

    def __init__(self, name, ide):
        self.name = name
        self.ide = ide

    def display(self):
        print(self.name)
        print(self.ide)


class Employee(Person):
    def __init__(self, name, ide, post, salary):
        self.post = post
        self.salary = salary
    Person.__init__(self, name, ide)


emp1 = Person("Hassan", "14347")
emp1.display()

emp2 = Employee("MUnene", "21/04609", "Snr dev", "200k")
emp2.display()
emp2.print()
