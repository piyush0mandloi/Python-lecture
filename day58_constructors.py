class Person:
    def __init__(self, Name, job):
        self.name = Name
        self.job = job
    def info(self):
        print(f"{self.name} is a {self.job} in Google")

a = Person("Piyush", "SDE1")
b = Person("Neeraj", "Giv Employee")
print(a.info())
print(b.info())