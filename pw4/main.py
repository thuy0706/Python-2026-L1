import curses
import input
import output

def main(stdscr):
    # Centralized data management
    students = []
    courses = []
    marks = {} 

    while True:
        stdscr.clear()
        stdscr.addstr("--- USTH Student Mark Management (PW4) ---\n")
        stdscr.addstr("1. Input Students\n")
        stdscr.addstr("2. Input Courses\n")
        stdscr.addstr("3. Input Marks\n")
        stdscr.addstr("4. List Students (Sorted by GPA)\n")
        stdscr.addstr("5. Show Marks\n")
        stdscr.addstr("6. Quit\n")
        stdscr.addstr("Select an option: ")
        
        curses.echo()
        choice = stdscr.getstr().decode('utf-8')
        curses.noecho()

        if choice == '1':
            input.input_students(stdscr, students)
        elif choice == '2':
            input.input_courses(stdscr, courses)
        elif choice == '3':
            input.input_marks(stdscr, students, courses, marks)
        elif choice == '4':
            output.list_students(stdscr, students, courses, marks)
        elif choice == '5':
            output.show_marks(stdscr, students, marks)
        elif choice == '6':
            break

if __name__ == "__main__":
    curses.wrapper(main)