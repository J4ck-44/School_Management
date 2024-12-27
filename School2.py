import random
from tabulate import tabulate

class Student:
    def __init__(self, name, email, phone, address):
        self.student_id = self.generate_unique_id()
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.list_of_courses = []

    def generate_unique_id(self):
        while True:
            unique_id = random.randint(1000, 9999)
            if not Management().validate_id(unique_id, Management().students):
                return unique_id

    def view_courses(self):
        return [course.view_course_details() for course in self.list_of_courses]

    def add_course(self, course):
        self.list_of_courses.append(course)

class Teacher:
    def __init__(self, name, email, phone, address):
        self.teacher_id = self.generate_unique_id()
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.list_of_courses = []
        self.list_of_batches = []

    def generate_unique_id(self):
        while True:
            unique_id = random.randint(1000, 9999)
            if not Management().validate_id(unique_id, Management().teachers):
                return unique_id

    def add_course(self, course):
        self.list_of_courses.append(course)

    def view_courses(self):
        return [course.view_course_details() for course in self.list_of_courses]

    def view_batches(self):
        return self.list_of_batches

class Course:
    def __init__(self, course_id, course_name, teacher, course_description):
        self.teacher = teacher
        self.course_id = course_id
        self.course_name = course_name
        self.course_description = course_description
        teacher.add_course(self)

    def view_course_details(self):
        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "course_description": self.course_description,
            "teacher": self.teacher.name
        }

class Management:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        if not self.validate_id(student.student_id, self.students):
            self.students.append(student)

    def add_teacher(self, teacher):
        if not self.validate_id(teacher.teacher_id, self.teachers):
            self.teachers.append(teacher)

    def add_course(self, course):
        if not self.validate_id(course.course_id, self.courses):
            self.courses.append(course)

    def validate_id(self, unique_id, collection):
        return any(
            (hasattr(item, 'student_id') and item.student_id == unique_id) or
            (hasattr(item, 'teacher_id') and item.teacher_id == unique_id) or
            (hasattr(item, 'course_id') and item.course_id == unique_id) for item in collection)

    def search_user(self, unique_id):
        for student in self.students:
            if student.student_id == unique_id:
                return student
        for teacher in self.teachers:
            if teacher.teacher_id == unique_id:
                return teacher
        return None

    def assign_course_to_student(self, student_id, course):
        student = self.search_user(student_id)
        if student and course.teacher:
            student.add_course(course)

    def display_student_details(self, student_id):
        student = self.search_user(student_id)
        if student:
            return {
                "Name": student.name,
                "Email": student.email,
                "Phone": student.phone,
                "Address": student.address,
                "Courses": student.view_courses()
            }

    def display_teacher_details(self, teacher_id):
        teacher = self.search_user(teacher_id)
        if teacher:
            return {
                "Name": teacher.name,
                "Email": teacher.email,
                "Phone": teacher.phone,
                "Address": teacher.address,
                "Courses": teacher.view_courses()
            }

def main():

    management = Management()


    student1 = Student("Ayush Sharma", "ayush1@gmail.com.com", "1276567569", "123 Waghodia")
    student2 = Student("Rishita Kumari", "rishita45@gmail.com.com", "9874365578", "456 Vadodara")


    management.add_student(student1)
    management.add_student(student2)

    teacher1 = Teacher("Jeet Jha", "jeetjha@gmail.com.com", "6556987998", "789 Vrindawan")
    teacher2 = Teacher("Pawan Patel", "pawan@gmail.com.com", "5598998321", "321 Limda")

    management.add_teacher(teacher1)
    management.add_teacher(teacher2)


    course1 = Course(101, "Python", teacher1, "A Python Project.")
    course2 = Course(102, "Java", teacher2, "OOPS with Java.")


    management.add_course(course1)
    management.add_course(course2)


    management.assign_course_to_student(student1.student_id, course1)
    management.assign_course_to_student(student2.student_id, course2)


    student_data = []
    for student in management.students:
        student_info = management.display_student_details(student.student_id)
        student_data.append([student_info["Name"], student_info["Email"], student_info["Phone"], student_info["Address"], ', '.join(course['course_name'] for course in student_info["Courses"])])

    print("Student Details:")
    print(tabulate(student_data, headers=["Name", "Email", "Phone", "Address", "Courses"]))

    teacher_data = []
    for teacher in management.teachers:
        teacher_info = management.display_teacher_details(teacher.teacher_id)
        teacher_data.append([teacher_info["Name"], teacher_info["Email"], teacher_info["Phone"], teacher_info["Address"], ', '.join(course['course_name'] for course in teacher_info["Courses"])])

    print("\nTeacher Details:")
    print(tabulate(teacher_data, headers=["Name", "Email", "Phone", "Address", "Courses"]))


if __name__ == "__main__":
    main()