class Course:
    def __init__(self, course_id, name, instructor):
        self.course_id = course_id
        self.name = name
        self.instructor = instructor
    
    def __str__(self):
        return f"{self.course_id}: {self.name} (Instructor: {self.instructor})"
    
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = []
    
    def enroll(self,course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            print(f"✅ {self.name} enrolled in {course.name}.")
        else:
            print(f"⚠️ {self.name} is already enrolled in {course.name}.")
    
    def view_courses(self):
        if not self.enrolled_courses:
            print(f"📝 {self.name} is not enrolled in any courses.")
        else:
            print(f"📝 {self.name}'s Enrolled Courses:")
            for course in self.enrolled_courses:
                print(f" -{course}")


class LMS:
    def __init__(self):
        self.courses = []
        self.students = []
    
    def add_course(self, course_id, name, instructor):
        course = Course(course_id, name, instructor)
        self.courses.append(course)
        print(f"✅ Course {name} added successfully.")
    
    def register_student(self, student_id, name):
        student = Student(student_id, name)
        self.students.append(student)
        print(f"✅ Student {name} registered successfully.")

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        print(f"⚠️ Student with ID {student_id} not found.")
        return None
    
    def find_course(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        print(f"⚠️ Course with ID {course_id} not found.")
        return None
    
    def enroll_student_in_course(self, student_id, course_id):
        student = self.find_student(student_id)
        course = self.find_course(course_id)
        
        if student and course:
            student.enroll(course)
        else:
            print("⚠️ Enrollment failed. Check student ID and course ID.")


def main():
    lms = LMS()
    while True:
        print("\n📚 Welcome to the Python LMS")
        print("1. Add Course")
        print("2. Register Student")
        print("3. Enroll Student in Course")
        print("4. View Student's Courses")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            cid = input("Course ID: ")
            cname = input("Course Name: ")
            instructor = input("Instructor Name: ")
            lms.add_course(cid, cname, instructor)

        elif choice == "2":
            sid = input("Student ID: ")
            sname = input("Student Name: ")
            lms.register_student(sid, sname)

        elif choice == "3":
            sid = input("Student ID: ")
            cid = input("Course ID: ")
            lms.enroll_student_in_course(sid, cid)

        elif choice == "4":
            sid = input("Student ID: ")
            student = lms.find_student(sid)
            if student:
                student.view_courses()
        elif choice == "7":
            print("Exiting LMS. Bye! 👋")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()