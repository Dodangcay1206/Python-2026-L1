import math
from domains import Student, Course

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

def input_number_of_students():
    return read_int("Enter number of students: ")

def input_student_info():
    new_students = []
    for i in range(input_number_of_students()):
        print(f"\nStudent {i + 1}:")
        s_id = input("  Enter ID: ")
        s_name = input("  Enter name: ")
        s_dob = input("  Enter DoB: ")
        new_students.append(Student(s_id, s_name, s_dob))
    return new_students

def input_number_of_courses():
    return read_int("Enter number of courses: ")

def input_course_info():
    new_courses = []
    for i in range(input_number_of_courses()):
        print(f"\nCourse {i + 1}:")
        c_id = input("  Enter course ID: ")
        c_name = input("  Enter course name: ")
        c_credit = read_float("  Enter course credit: ")
        new_courses.append(Course(c_id, c_name, c_credit))
    return new_courses

def input_course_id(prompt="\nEnter course ID: "):
    return input(prompt)

def input_mark_for(student):
    raw_mark = read_float(f"Mark for {student.name} (ID: {student.student_id}): ")
    return math.floor(raw_mark * 10) / 10