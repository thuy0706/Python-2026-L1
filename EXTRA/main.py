from student_module import Student, Course, Mark

from file_module import (
    save_students_txt,
    load_students_txt,
    save_pickle,
    load_pickle,
    compress_file,
    decompress_file,
    export_students_csv,
    export_courses_csv,
    export_marks_csv,
    load_csv_files,
    query_students
)


# =====================================
# CREATE DATA
# =====================================

students = [
    Student("S001", "Mr. Volunteers", "2005-01-10"),
    Student("S002", "Alice", "2005-03-15"),
    Student("S003", "Bob", "2005-06-20"),
    Student("S004", "David", "2005-09-12")
]


courses = [
    Course("C001", "Python"),
    Course("C002", "Database"),
    Course("C003", "Algorithms")
]


marks = [
    Mark("S001", "C001", 8.5),
    Mark("S001", "C002", 9.0),
    Mark("S002", "C001", 7.5),
    Mark("S002", "C002", 8.0),
    Mark("S003", "C001", 6.5),
    Mark("S003", "C003", 7.0),
    Mark("S004", "C002", 9.5)
]


# =====================================
# 1. TEXT FILE
# =====================================

print("===== TEXT FILE =====")

save_students_txt(students)

loaded_students = load_students_txt()

for student in loaded_students:
    print(
        student.student_id,
        student.name,
        student.dob
    )


# =====================================
# 2. PICKLE
# =====================================

print("\n===== PICKLE =====")

save_pickle(students)

loaded_students = load_pickle()

for student in loaded_students:
    print(
        student.student_id,
        student.name,
        student.dob
    )


# =====================================
# 3. COMPRESS
# =====================================

print("\n===== COMPRESS =====")

compress_file("students.dat")

# Optional:
# decompress_file("students.dat.gz")


# =====================================
# 4. EXPORT CSV
# =====================================

print("\n===== EXPORT CSV =====")

export_students_csv(students)
export_courses_csv(courses)
export_marks_csv(marks)


# =====================================
# 5. LOAD CSV USING PANDAS
# =====================================

print("\n===== LOAD CSV USING PANDAS =====")

students_df, courses_df, marks_df = load_csv_files()


print("\nStudents:")
print(students_df)

print("\nCourses:")
print(courses_df)

print("\nMarks:")
print(marks_df)


# =====================================
# 6. EXTRA QUERY
# =====================================

print("\n===== EXTRA QUERY =====")

query_students(students_df)