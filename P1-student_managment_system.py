class Student:
    def __init__(self, roll, name, age,course):
        self.roll = roll
        self.name = name
        self.age = age
        self.course = course
    
    def display(self):
        print(f"Roll No: {self.roll}, Name: {self.name}, Age: {self.age}, Course: {self.course}")

class StudentManager:
    def __init__(self):
        self.students = []
    
    def add_students(self):
        roll = input("Enter the Roll No: ")
        name = input("Enter Name: ")
        age = input("Enter the Age: ")
        course = input("Enter the Course: ")
        student = Student(roll, name, age, course)
        self.students.append(student)
        print("✅ Student Added successfully.\n")
    
    def display_all(self):
        if not self.students:
            print("⚠️ No students found.")
        else:
            print("📃 List of Students")
            for student in self.students:
                student.display()
            print()
    
    def search_student(self):
        roll = input("Enter roll no to search: ")
        found = False
        for student in self.students:
            if student.roll == roll:
                print("✅ Student Found: ")
                student.display()
                found = True
                break
        if not found:
            print("❌ Student not found.\n")

    def delete_student(self):
        roll = input("Enter roll no to delete: ")
        for student in self.students:
            if student.roll == roll:
                self.students.remove(student)
                print("Student deleted successfully.\n")
                return
        print("❌ Student not found.\n")

def menu():
    manager = StudentManager()
    while True:
        print("=== Student Management System")
        print('1. Add Students')
        print("2. Display All Students")
        print("3. Search student by roll no")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your Choice(1-5): ")

        if choice=='1':
            manager.add_students()
        elif choice=='2':
            manager.display_all()
        elif choice=='3':
            manager.search_student()
        elif choice=='4':
            manager.delete_student()
        elif choice=='5':
            print("👋🙋‍♂️Exiting...")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

menu()