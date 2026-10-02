# -*- coding: utf-8 -*-
"""Practical work 1: Student mark management"""

students = []  # Stores student information - tuple (id, name, dob)
courses = []   # Stores course information - tuple (id, name)
marks = {}     # marks[course_id][student_id] = mark


# ---------- HELPERS ----------
def read_int(prompt):
    """Keep asking until the user enters a valid non-negative integer."""students = []  
courses = []   
marks = {}     

def read_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative number!")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer!")

def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")


def course_exists(course_id):
    return any(c[0] == course_id for c in courses)

def input_number_of_students():
    return read_int("Enter number of students: ")

def input_student_info():
    for i in range(input_number_of_students()):
        print(f"\nStudent {i + 1}:")
        s_id = input("  Enter ID: ")
        s_name = input("  Enter name: ")
        s_dob = input("  Enter DoB: ")
        students.append((s_id, s_name, s_dob))

# ---------- COURSES ----------
def input_number_of_courses():
    return read_int("Enter number of courses: ")

def input_course_info():
    for i in range(input_number_of_courses()):
        print(f"\nCourse {i + 1}:")
        c_id = input("  Enter course ID: ")
        c_name = input("  Enter course name: ")
        courses.append((c_id, c_name))

# ---------- LIST ----------
def list_students():
    print("\n--- Student List ---")
    if not students:
        print("No students available.")
        return
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

def list_courses():
    print("\n--- Course List ---")
    if not courses:
        print("No courses available.")
        return
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

# ---------- MARKS ----------
def input_marks():
    if not courses:
        print("Please add courses first!")
        return
    if not students:
        print("Please add students first!")
        return
    list_courses()
    course_id = input("\nEnter course ID to give marks: ")
    if not course_exists(course_id):
        print("Course ID not found!")
        return
    course_marks = marks.setdefault(course_id, {})  # keep old marks
    for student in students:
        s_id = student[0]
        s_name = student[1]
        course_marks[s_id] = read_float(f"Mark for {s_name} (ID: {s_id}): ")

def show_student_marks():
    if not marks:
        print("No marks entered yet.")
        return
    list_courses()
    course_id = input("\nEnter course ID to view marks: ")
    if course_id not in marks:
        print("No marks found for this course ID.")
        return
    print(f"\n--- Marks for course {course_id} ---")
    for student in students:
        s_id = student[0]
        s_name = student[1]
        if s_id in marks[course_id]:
            print(f"ID: {s_id} - Name: {s_name} - Mark: {marks[course_id][s_id]}")
        else:
            print(f"ID: {s_id} - Name: {s_name} - Mark: (not entered)")

def main():
    while True:
        print("""
=== MENU ===
1. Input student information
2. Input course information
3. Input marks for a course
4. List courses
5. List students
6. Show marks for a course
0. Exit
""")
        choice = input("Your choice: ")
        if choice == "1":
            input_student_info()
        elif choice == "2":
            input_course_info()
        elif choice == "3":
            input_marks()
        elif choice == "4":
            list_courses()
        elif choice == "5":
            list_students()
        elif choice == "6":
            show_student_marks()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative number!")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer!")


def read_float(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")


def course_exists(course_id):
    return any(c[0] == course_id for c in courses)


# ---------- STUDENTS ----------
def input_number_of_students():
    return read_int("Enter number of students: ")


def input_student_info():
    for i in range(input_number_of_students()):
        print(f"\nStudent {i + 1}:")
        s_id = input("  Enter ID: ")
        s_name = input("  Enter name: ")
        s_dob = input("  Enter DoB: ")
        students.append((s_id, s_name, s_dob))


# ---------- COURSES ----------
def input_number_of_courses():
    return read_int("Enter number of courses: ")


def input_course_info():
    for i in range(input_number_of_courses()):
        print(f"\nCourse {i + 1}:")
        c_id = input("  Enter course ID: ")
        c_name = input("  Enter course name: ")
        courses.append((c_id, c_name))


# ---------- LIST ----------
def list_students():
    print("\n--- Student List ---")
    if not students:
        print("No students available.")
        return
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")


def list_courses():
    print("\n--- Course List ---")
    if not courses:
        print("No courses available.")
        return
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")


# ---------- MARKS ----------
def input_marks():
    if not courses:
        print("Please add courses first!")
        return
    if not students:
        print("Please add students first!")
        return
    list_courses()
    course_id = input("\nEnter course ID to give marks: ")
    if not course_exists(course_id):
        print("Course ID not found!")
        return
    course_marks = marks.setdefault(course_id, {})  # keep old marks
    for student in students:
        s_id = student[0]
        s_name = student[1]
        course_marks[s_id] = read_float(f"Mark for {s_name} (ID: {s_id}): ")


def show_student_marks():
    if not marks:
        print("No marks entered yet.")
        return
    list_courses()
    course_id = input("\nEnter course ID to view marks: ")
    if course_id not in marks:
        print("No marks found for this course ID.")
        return
    print(f"\n--- Marks for course {course_id} ---")
    for student in students:
        s_id = student[0]
        s_name = student[1]
        if s_id in marks[course_id]:
            print(f"ID: {s_id} - Name: {s_name} - Mark: {marks[course_id][s_id]}")
        else:
            print(f"ID: {s_id} - Name: {s_name} - Mark: (not entered)")


# ---------- MAIN ----------
def main():
    while True:
        print("""
=== MENU ===
1. Input student information
2. Input course information
3. Input marks for a course
4. List courses
5. List students
6. Show marks for a course
0. Exit
""")
        choice = input("Your choice: ")
        if choice == "1":
            input_student_info()
        elif choice == "2":
            input_course_info()
        elif choice == "3":
            input_marks()
        elif choice == "4":
            list_courses()
        elif choice == "5":
            list_students()
        elif choice == "6":
            show_student_marks()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
