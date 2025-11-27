# Parent class 1
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

# Parent class 2
class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id

    def show_id(self):
        print(f"My employee ID is {self.emp_id}")

# Child class inherits from both Person and Employee
class Manager(Person, Employee):
    def __init__(self, name, emp_id, department):
        Person.__init__(self, name)
        Employee.__init__(self, emp_id)
        self.department = department

    def show_department(self):
        print(f"I manage the {self.department} department")

# Using the class
m = Manager("Piyush", 101, "IT")
m.greet()
m.show_id()
m.show_department()
