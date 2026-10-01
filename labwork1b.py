# Practical Work 1: Student Mark Management


students = []
courses = []
marks = {}


# =========================
# Input functions
# =========================

def input_students():
    n = int(input("Enter number of students: "))

    for i in range(n):
        print(f"\nEnter information for student {i + 1}")

        student_id = input("ID: ")
        name = input("Name: ")
        dob = input("Date of Birth: ")

        student = {
            "id": student_id,
            "name": name,
            "dob": dob
        }

        students.append(student)


def input_courses():
    n = int(input("\nEnter number of courses: "))

    for i in range(n):
        print(f"\nEnter information for course {i + 1}")

        course_id = input("Course ID: ")
        course_name = input("Course name: ")

        course = {
            "id": course_id,
            "name": course_name
        }

        courses.append(course)


def input_marks():
    if len(courses) == 0:
        print("No courses available.")
        return

    print("\nCourses:")
    list_courses()

    course_id = input("Enter course ID: ")

    # Check whether the course exists
    course_exists = False

    for course in courses:
        if course["id"] == course_id:
            course_exists = True
            break

    if not course_exists:
        print("Course not found.")
        return

    marks[course_id] = {}

    print("\nEnter marks for students:")

    for student in students:
        mark = float(
            input(f"Enter mark for {student['name']} ({student['id']}): ")
        )

        marks[course_id][student["id"]] = mark


# =========================
# Listing functions
# =========================

def list_courses():
    print("\n===== COURSES =====")

    for course in courses:
        print(
            f"ID: {course['id']} | "
            f"Name: {course['name']}"
        )


def list_students():
    print("\n===== STUDENTS =====")

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"DoB: {student['dob']}"
        )


def show_student_marks():
    if len(courses) == 0:
        print("No courses available.")
        return

    print("\nCourses:")
    list_courses()

    course_id = input("Enter course ID: ")

    if course_id not in marks:
        print("No marks found for this course.")
        return

    print(f"\n===== MARKS FOR COURSE {course_id} =====")

    for student in students:
        student_id = student["id"]

        if student_id in marks[course_id]:
            print(
                f"{student['name']} ({student_id}): "
                f"{marks[course_id][student_id]}"
            )


# =========================
# Main program
# =========================

input_students()

input_courses()

input_marks()

print("\n")
list_courses()

print("\n")
list_students()

print("\n")
show_student_marks()