def display_students(students):
    print("\n--- Student List ---")
    for s in students:
        print(f"ID: {s.id} | Name: {s.name} | DoB: {s.dob}")

def display_courses(courses):
    print("\n--- Course List ---")
    for c in courses:
        print(f"ID: {c.id} | Name: {c.name} | Credits: {c.credits}")

def display_marks(marks):
    print("\n--- Mark List ---")
    for m in marks:
        print(f"Course ID: {m.course_id} | Student ID: {m.student_id} | Mark: {m.mark}")

def display_all(students, courses, marks):
    display_students(students)
    display_courses(courses)
    display_marks(marks)