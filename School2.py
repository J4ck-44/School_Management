import random
class Student:
    def __init__(self, name, email, phone, address):
        self.student_id = self.generate_unique_id()  # Generate a unique ID
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.list_of_courses = []
    def generate_unique_id(self):
        # Generate a random ID and ensure it's unique
        while True:
            unique_id = random.randint(1000, 9999)  # Generate a random ID between 1000 and 9999
            if not Management().validate_id(unique_id, Management().students):  # Check for uniqueness
                return unique_id
    def view_courses(self):
        return self.list_of_courses
    def add_course(self, course):
        self.list_of_courses.append(course)
class Teacher:
    def __init__(self, name, email, phone, address):
        self.teacher_id = self.generate_unique_id()  # Generate a unique ID
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.list_of_courses = []
        self.list_of_batches = []
    def generate_unique_id(self):
        # Generate a random ID and ensure it's unique
        while True:
            unique_id = random.randint(1000, 9999)  # Generate a random ID between 1000 and 9999
            if not Management().validate_id(unique_id, Management().teachers):  # Check for uniqueness
                return unique_id
    def add_course(self, course):
        self.list_of_courses.append(course)
    def view_courses(self):
        return self.list_of_courses
    def view_batches(self):
        return self.list_of_batches
class Course:
    def __init__(self, course_id, course_name, teachers, course_description):
        self.teachers = None
        self.course_id = course_id
        self.course_name = course_name
        self.course_description = course_description
    def assign_course(self, teacher):
        self.teachers = teacher
    def view_course_details(self):
        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "course_description": self.course_description,
            "teacher": self.teachers
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
            item.student_id == unique_id or item.teacher_id == unique_id or item.course_id == unique_id for item in
            collection)
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
        if student and course.teachers:
            student.add_course(course)
    def display_student_details(self, student_id):
        student = self.search_user(student_id)
        if student:
            return {
                "name": student.name,
                "courses": student.view_courses()
            }
    def display_teacher_details(self, teacher_id):
        teacher = self.search_user(teacher_id)
        if teacher:
            return {
                "name": teacher.name,
                "courses": teacher.view_courses()
            }
