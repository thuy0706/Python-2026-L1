from domains.student import Student
from domains.course import Course
from domains.mark import Mark

def input_number_of_students():
    return int(input("Enter number of students: "))

def input_student_info():
    student_id = input("Student ID: ")
    name = input("Name: ")
    dob = input("DoB: ")
    return Student(student_id, name, dob)

def input_number_of_courses():
    return int(input("Enter number of courses: "))

def input_course_info():
    course_id = input("Course ID: ")
    name = input("Course Name: ")
    credits = int(input("Credits: "))
    return Course(course_id, name, credits)

def input_marks(students, courses):
    marks = {}
    for course in courses:
        print(f"Enter marks for {course.name}:")
        marks[course.id] = {}
        for student in students:
            mark = float(input(f"Mark for {student.name}: "))
            marks[course.id][student.id] = mark
    return marks