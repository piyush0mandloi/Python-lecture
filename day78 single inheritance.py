class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")


a = Animal("SomeAnimal")
a.speak()  # Output: SomeAnimal makes a sound

d = Dog("Buddy")
d.speak()  # Output: Buddy barks


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"{self.name} earns {self.salary} USD")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def show(self):
        super().show()
        print(f"Manages team of {self.team_size} people")

m = Manager("Alice", 8000, 5)
m.show()

