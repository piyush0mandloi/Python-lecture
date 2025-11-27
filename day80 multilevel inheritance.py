 # Grandparent class
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

# Parent class
class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

    def show_id(self):
        print(f"My employee ID is {self.emp_id}")

# Child class
class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def show_department(self):
        print(f"I manage the {self.department} department")

# Using the class
m = Manager("Piyush", 101, "IT")
m.greet()             # From Person (grandparent)
m.show_id()           # From Employee (parent)
m.show_department()   # From Manager (child)
