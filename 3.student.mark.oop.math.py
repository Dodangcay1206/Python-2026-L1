# -*- coding: utf-8 -*-

import math
import numpy as np
import curses

# Stores student information - Tuple
students = []

# Stores course information:
# (course_id, course_name, credits)
courses = []

# marks[course_id][student_id] = mark
marks = {}


# ---------- STUDENTS ----------

def input_number_of_students(stdscr):
    stdscr.addstr("Enter number of students: ")
    stdscr.refresh()
    return int(stdscr.getstr().decode("utf-8"))


def input_student_info(stdscr):
    try:
        number = input_number_of_students(stdscr)

        for i in range(number):
            stdscr.addstr(f"\nStudent {i + 1}:\n")

            stdscr.addstr("  Enter ID: ")
            stdscr.refresh()
            s_id = stdscr.getstr().decode("utf-8")

            stdscr.addstr("  Enter name: ")
            stdscr.refresh()
            s_name = stdscr.getstr().decode("utf-8")

            stdscr.addstr("  Enter DoB: ")
            stdscr.refresh()
            s_dob = stdscr.getstr().decode("utf-8")

            students.append((s_id, s_name, s_dob))

        stdscr.addstr("\nStudents added successfully!")
    except ValueError:
        stdscr.addstr("\nPlease enter a valid number!")


# ---------- COURSES ----------

def input_number_of_courses(stdscr):
    stdscr.addstr("Enter number of courses: ")
    stdscr.refresh()
    return int(stdscr.getstr().decode("utf-8"))


def input_course_info(stdscr):
    try:
        number = input_number_of_courses(stdscr)

        for i in range(number):
            stdscr.addstr(f"\nCourse {i + 1}:\n")

            stdscr.addstr("  Enter course ID: ")
            stdscr.refresh()
            c_id = stdscr.getstr().decode("utf-8")

            stdscr.addstr("  Enter course name: ")
            stdscr.refresh()
            c_name = stdscr.getstr().decode("utf-8")

            stdscr.addstr("  Enter credits: ")
            stdscr.refresh()
            credits = int(stdscr.getstr().decode("utf-8"))

            courses.append((c_id, c_name, credits))

        stdscr.addstr("\nCourses added successfully!")
    except ValueError:
        stdscr.addstr("\nPlease enter valid input!")


# ---------- LIST ----------

def list_students(stdscr):
    stdscr.addstr("\n--- Student List ---\n")

    if not students:
        stdscr.addstr("No students available.")
        return

    for student in students:
        stdscr.addstr(
            f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}\n"
        )


def list_courses(stdscr):
    stdscr.addstr("\n--- Course List ---\n")

    if not courses:
        stdscr.addstr("No courses available.")
        return

    for course in courses:
        stdscr.addstr(
            f"ID: {course[0]}, Name: {course[1]}, Credits: {course[2]}\n"
        )


# ---------- MARKS ----------

def input_marks(stdscr):
    if not courses:
        stdscr.addstr("Please add courses first!")
        return

    if not students:
        stdscr.addstr("Please add students first!")
        return

    list_courses(stdscr)

    stdscr.addstr("\nEnter course ID to give marks: ")
    stdscr.refresh()
    course_id = stdscr.getstr().decode("utf-8")

    # Check whether the course exists
    course_exists = False
    for course in courses:
        if course[0] == course_id:
            course_exists = True
            break

    if not course_exists:
        stdscr.addstr("Course ID not found.")
        return

    # Keep old marks instead of deleting them
    if course_id not in marks:
        marks[course_id] = {}

    for student in students:
        s_id = student[0]
        s_name = student[1]

        while True:
            try:
                stdscr.addstr(
                    f"Mark for {s_name} (ID: {s_id}): "
                )
                stdscr.refresh()

                mark = float(stdscr.getstr().decode("utf-8"))

                if mark < 0 or mark > 10:
                    stdscr.addstr(
                        "Mark must be between 0 and 10.\n"
                    )
                    continue

                # Round DOWN to 1 decimal place
                mark = math.floor(mark * 10) / 10

                marks[course_id][s_id] = mark
                break

            except ValueError:
                stdscr.addstr("Please enter a valid mark.\n")

    stdscr.addstr("\nMarks entered successfully!")


# ---------- SHOW MARKS ----------

def show_student_marks(stdscr):
    if not marks:
        stdscr.addstr("No marks entered yet.")
        return

    list_courses(stdscr)

    stdscr.addstr("\nEnter course ID to view marks: ")
    stdscr.refresh()
    course_id = stdscr.getstr().decode("utf-8")

    if course_id not in marks:
        stdscr.addstr("No marks found for this course ID.")
        return

    stdscr.addstr(f"\n--- Marks for course {course_id} ---\n")

    for student in students:
        s_id = student[0]
        s_name = student[1]

        if s_id in marks[course_id]:
            stdscr.addstr(
                f"ID: {s_id} - Name: {s_name} "
                f"- Mark: {marks[course_id][s_id]}\n"
            )


# ---------- GPA ----------

def calculate_gpa(student_id):
    student_marks = []
    student_credits = []

    for course in courses:
        course_id = course[0]
        credits = course[2]

        if course_id in marks and student_id in marks[course_id]:
            student_marks.append(marks[course_id][student_id])
            student_credits.append(credits)

    if not student_marks:
        return 0.0

    # Convert lists to NumPy arrays
    mark_array = np.array(student_marks)
    credit_array = np.array(student_credits)

    # Weighted average
    gpa = np.average(mark_array, weights=credit_array)

    return round(float(gpa), 2)


def show_student_gpa(stdscr):
    if not students:
        stdscr.addstr("No students available.")
        return

    stdscr.addstr("\n--- Student GPA ---\n")

    for student in students:
        gpa = calculate_gpa(student[0])
        stdscr.addstr(
            f"ID: {student[0]} - Name: {student[1]} - GPA: {gpa}\n"
        )


# ---------- SORT BY GPA ----------

def sort_students_by_gpa(stdscr):
    if not students:
        stdscr.addstr("No students available.")
        return

    # Sort by GPA from highest to lowest
    sorted_students = sorted(
        students,
        key=lambda student: calculate_gpa(student[0]),
        reverse=True
    )

    stdscr.addstr("\n--- Students sorted by GPA ---\n")

    for student in sorted_students:
        gpa = calculate_gpa(student[0])

        stdscr.addstr(
            f"ID: {student[0]} - "
            f"Name: {student[1]} - "
            f"GPA: {gpa}\n"
        )


# ---------- CURSES MENU ----------

def main_menu(stdscr):
    curses.curs_set(1)

    while True:
        stdscr.clear()

        stdscr.addstr(
            "========================================\n"
        )
        stdscr.addstr(
            "       STUDENT MARK MANAGEMENT\n"
        )
        stdscr.addstr(
            "========================================\n"
        )
        stdscr.addstr("1. Input student information\n")
        stdscr.addstr("2. Input course information\n")
        stdscr.addstr("3. Input marks for a course\n")
        stdscr.addstr("4. List courses\n")
        stdscr.addstr("5. List students\n")
        stdscr.addstr("6. Show marks for a course\n")
        stdscr.addstr("7. Show student GPA\n")
        stdscr.addstr("8. Sort students by GPA descending\n")
        stdscr.addstr("0. Exit\n")
        stdscr.addstr(
            "========================================\n"
        )
        stdscr.addstr("Your choice: ")
        stdscr.refresh()

        choice = stdscr.getstr().decode("utf-8")

        stdscr.clear()

        if choice == "1":
            input_student_info(stdscr)

        elif choice == "2":
            input_course_info(stdscr)

        elif choice == "3":
            input_marks(stdscr)

        elif choice == "4":
            list_courses(stdscr)

        elif choice == "5":
            list_students(stdscr)

        elif choice == "6":
            show_student_marks(stdscr)

        elif choice == "7":
            show_student_gpa(stdscr)

        elif choice == "8":
            sort_students_by_gpa(stdscr)

        elif choice == "0":
            stdscr.addstr("Goodbye!")
            stdscr.refresh()
            break

        else:
            stdscr.addstr("Invalid choice!")

        if choice != "0":
            stdscr.addstr("\n\nPress Enter to continue...")
            stdscr.refresh()
            stdscr.getch()


# ---------- MAIN ----------

def main():
    curses.wrapper(main_menu)


if __name__ == "__main__":
    main()
