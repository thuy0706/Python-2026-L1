import os
import zipfile
from domains.student import Student
from domains.course import Course
from domains.mark import Mark

def compress_data():
    files = ["students.txt", "courses.txt", "marks.txt"]
    with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            if os.path.exists(file):
                zipf.write(file)
                os.remove(file)

def load_data():
    students = []
    courses = []
    marks = []

    if os.path.exists("students.dat"):
        with zipfile.ZipFile("students.dat", "r") as zipf:
            zipf.extractall()

        if os.path.exists("students.txt"):
            with open("students.txt", "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        s_id, name, dob = line.split(",")
                        students.append(Student(s_id, name, dob))

        if os.path.exists("courses.txt"):
            with open("courses.txt", "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        c_id, name, credits = line.split(",")
                        courses.append(Course(c_id, name, int(credits)))

        if os.path.exists("marks.txt"):
            with open("marks.txt", "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        c_id, s_id, score = line.split(",")
                        marks.append(Mark(s_id, c_id, float(score)))

    return students, courses, marks