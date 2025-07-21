class Person:
    name = "Piyush"
    job = "SDE1"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.job} in Google")

a = Person()
b = Person()
a.name = "Neeraj"
print(a.name)
print(b.name)
print(a.info())
print(b.info())