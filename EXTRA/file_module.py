import pickle
import gzip
import pandas as pd


# =========================
# TEXT FILE
# =========================

def save_students_txt(students, filename="students.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for student in students:
            file.write(
                f"{student.student_id},{student.name},{student.dob}\n"
            )


def load_students_txt(filename="students.txt"):
    students = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            student_id, name, dob = line.strip().split(",")

            from student_module import Student
            students.append(Student(student_id, name, dob))

    return students


# =========================
# PICKLE
# =========================

def save_pickle(students, filename="students.dat"):
    with open(filename, "wb") as file:
        pickle.dump(students, file)


def load_pickle(filename="students.dat"):
    with open(filename, "rb") as file:
        return pickle.load(file)


# =========================
# COMPRESS
# =========================

def compress_file(filename="students.dat"):
    output_file = filename + ".gz"

    with open(filename, "rb") as source:
        with gzip.open(output_file, "wb") as target:
            target.write(source.read())

    print("Compressed file:", output_file)


def decompress_file(filename="students.dat.gz"):
    output_file = "students_decompressed.dat"

    with gzip.open(filename, "rb") as source:
        with open(output_file, "wb") as target:
            target.write(source.read())

    print("Decompressed file:", output_file)


# =========================
# EXPORT STUDENTS TO CSV
# =========================

def export_students_csv(students, filename="students.csv"):

    data = []

    for student in students:
        data.append({
            "student_id": student.student_id,
            "name": student.name,
            "dob": student.dob
        })

    df = pd.DataFrame(data)

    df.to_csv(filename, index=False)

    print("Exported:", filename)


# =========================
# EXPORT COURSES TO CSV
# =========================

def export_courses_csv(courses, filename="courses.csv"):

    data = []

    for course in courses:
        data.append({
            "course_id": course.course_id,
            "name": course.name
        })

    df = pd.DataFrame(data)

    df.to_csv(filename, index=False)

    print("Exported:", filename)


# =========================
# EXPORT MARKS TO CSV
# =========================

def export_marks_csv(marks, filename="marks.csv"):

    data = []

    for mark in marks:
        data.append({
            "student_id": mark.student_id,
            "course_id": mark.course_id,
            "mark": mark.mark
        })

    df = pd.DataFrame(data)

    df.to_csv(filename, index=False)

    print("Exported:", filename)


# =========================
# LOAD CSV INTO DATAFRAME
# =========================

def load_csv_files():

    students_df = pd.read_csv("students.csv")
    courses_df = pd.read_csv("courses.csv")
    marks_df = pd.read_csv("marks.csv")

    return students_df, courses_df, marks_df


# =========================
# EXTRA QUERY FUNCTION
# =========================

def query_students(df):

    print("\nStudent DataFrame:")
    print(df)

    print("\nExample condition:")
    print("name == 'Mr. Volunteers'")

    condition = input("\nEnter your condition: ")

    try:
        result = df.query(condition)

        print("\nQuery result:")
        print(result)

    except Exception as e:
        print("Invalid condition!")
        print("Error:", e)