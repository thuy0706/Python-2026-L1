import os

def write_students_to_file(students):
    with open("students.txt", "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s.id},{s.name},{s.dob}\n")

def write_courses_to_file(courses):
    with open("courses.txt", "w", encoding="utf-8") as f:
        for c in courses:
            f.write(f"{c.id},{c.name},{c.credits}\n")

def write_marks_to_file(marks):
    with open("marks.txt", "w", encoding="utf-8") as f:
        for m in marks:
            f.write(f"{m.course_id},{m.student_id},{m.mark}\n")

def input_students(students):
    count = int(input("Enter number of students: "))
    for _ in range(count):
        s_id = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("DoB: ")
        from domains.student import Student
        students.append(Student(s_id, name, dob))
    write_students_to_file(students)

def input_courses(courses):
    count = int(input("Enter number of courses: "))
    for _ in range(count):
        c_id = input("Course ID: ")
        name = input("Course Name: ")
        credits = int(input("Credits: "))
        from domains.course import Course
        courses.append(Course(c_id, name, credits))
    write_courses_to_file(courses)

def input_marks(marks, students, courses):
    c_id = input("Enter Course ID to input marks: ")
    for s in students:
        score = float(input(f"Enter mark for student {s.name} ({s.id}): "))
        from domains.mark import Mark
        marks.append(Mark(s.id, c_id, score))
    write_marks_to_file(marks)