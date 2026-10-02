from persistence import load_data, compress_data
import input as in_mod
import output as out_mod

def main():
    students, courses, marks = load_data()

    while True:
        print("\n--- MENU ---")
        print("1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks")
        print("4. Display All")
        print("0. Exit and Save")
        
        choice = input("Your choice: ")

        if choice == "1":
            in_mod.input_students(students)
        elif choice == "2":
            in_mod.input_courses(courses)
        elif choice == "3":
            in_mod.input_marks(marks, students, courses)
        elif choice == "4":
            out_mod.display_all(students, courses, marks)
        elif choice == "0":
            compress_data()
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()