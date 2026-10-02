import math
import sys

import numpy as np

try:
    import curses
except ImportError:  
    curses = None

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}"

class Course:
    def __init__(self, course_id, name, credit):
        self.course_id = course_id
        self.name = name
        self.credit = credit

    def __str__(self):
        return f"ID: {self.course_id}, Name: {self.name}, Credit: {self.credit}"

class StudentMarkManager:
    def __init__(self):
        self.students = []          
        self.courses = []           
        self.marks = {}             

    # ---- small helpers -----------------------------------------------
    @staticmethod
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

    @staticmethod
    def read_float(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number!")

    def find_course(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    # ---- input ----------------------------------------------------------
    def input_student_info(self):
        n = self.read_int("Enter number of students: ")
        for i in range(n):
            print(f"\nStudent {i + 1}:")
            s_id = input("  Enter ID: ")
            s_name = input("  Enter name: ")
            s_dob = input("  Enter DoB: ")
            self.students.append(Student(s_id, s_name, s_dob))

    def input_course_info(self):
        n = self.read_int("Enter number of courses: ")
        for i in range(n):
            print(f"\nCourse {i + 1}:")
            c_id = input("  Enter course ID: ")
            c_name = input("  Enter course name: ")
            c_credit = self.read_float("  Enter course credit: ")
            self.courses.append(Course(c_id, c_name, c_credit))

    def input_marks(self):
        if not self.courses:
            print("Please add courses first!")
            return
        if not self.students:
            print("Please add students first!")
            return
        self.list_courses()
        course_id = input("\nEnter course ID to give marks: ")
        if self.find_course(course_id) is None:
            print("Course ID not found!")
            return
        course_marks = self.marks.setdefault(course_id, {})
        for student in self.students:
            raw_mark = self.read_float(
                f"Mark for {student.name} (ID: {student.student_id}): "
            )
            rounded_mark = math.floor(raw_mark * 10) / 10
            course_marks[student.student_id] = rounded_mark

    def list_students(self):
        print("\n--- Student List ---")
        if not self.students:
            print("No students available.")
            return
        for student in self.students:
            print(student)

    def list_courses(self):
        print("\n--- Course List ---")
        if not self.courses:
            print("No courses available.")
            return
        for course in self.courses:
            print(course)

    def show_student_marks(self):
        if not self.marks:
            print("No marks entered yet.")
            return
        self.list_courses()
        course_id = input("\nEnter course ID to view marks: ")
        if course_id not in self.marks:
            print("No marks found for this course ID.")
            return
        print(f"\n--- Marks for course {course_id} ---")
        for student in self.students:
            s_id = student.student_id
            if s_id in self.marks[course_id]:
                print(f"ID: {s_id} - Name: {student.name} - Mark: {self.marks[course_id][s_id]}")
            else:
                print(f"ID: {s_id} - Name: {student.name} - Mark: (not entered)")

    # ---- GPA (numpy) --------------------------------------------------
    def calculate_gpa(self, student_id):
        """Credit-weighted average mark for one student, using numpy.
        Returns None if the student has no marks yet."""
        credits = []
        marks = []
        for course in self.courses:
            course_marks = self.marks.get(course.course_id, {})
            if student_id in course_marks:
                credits.append(course.credit)
                marks.append(course_marks[student_id])
        if not credits:
            return None
        credits_arr = np.array(credits, dtype=float)
        marks_arr = np.array(marks, dtype=float)
        gpa = np.sum(credits_arr * marks_arr) / np.sum(credits_arr)
        return float(gpa)

    def show_gpa_ranking(self):
        if not self.students:
            print("No students available.")
            return
        ranking = []
        for student in self.students:
            gpa = self.calculate_gpa(student.student_id)
            if gpa is not None:
                ranking.append((student, gpa))
        if not ranking:
            print("No student has marks yet.")
            return
        # sort by GPA, descending
        ranking.sort(key=lambda pair: pair[1], reverse=True)
        print("\n--- GPA Ranking (descending) ---")
        for rank, (student, gpa) in enumerate(ranking, start=1):
            print(f"{rank}. {student.name} (ID: {student.student_id}) - GPA: {gpa:.2f}")

def _draw_banner(stdscr, lines):
    curses.curs_set(0)
    stdscr.clear()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    height, width = stdscr.getmaxyx()
    box_height = len(lines) + 4
    box_width = max(len(line) for line in lines) + 6
    box_height = min(box_height, height)
    box_width = min(box_width, width)
    start_y = max((height - box_height) // 2, 0)
    start_x = max((width - box_width) // 2, 0)

    win = curses.newwin(box_height, box_width, start_y, start_x)
    win.bkgd(" ", curses.color_pair(1))
    win.border()
    for i, line in enumerate(lines):
        win.addstr(2 + i, 3, line[: box_width - 6])
    win.refresh()
    win.getch()

def show_banner(lines):
    if curses is None or not sys.stdout.isatty():
        print("=" * 40)
        for line in lines:
            print(line.center(40))
        print("=" * 40)
        return
    try:
        curses.wrapper(_draw_banner, lines)
    except curses.error:
        print("=" * 40)
        for line in lines:
            print(line.center(40))
        print("=" * 40)

def main():
    show_banner(["STUDENT MARK MANAGEMENT", "Practical Work 3", "Press any key to start"])

    manager = StudentMarkManager()
    while True:
        print("""
=== MENU ===
1. Input student information
2. Input course information
3. Input marks for a course
4. List courses
5. List students
6. Show marks for a course
7. Show GPA ranking (descending)
0. Exit
""")
        choice = input("Your choice: ")
        if choice == "1":
            manager.input_student_info()
        elif choice == "2":
            manager.input_course_info()
        elif choice == "3":
            manager.input_marks()
        elif choice == "4":
            manager.list_courses()
        elif choice == "5":
            manager.list_students()
        elif choice == "6":
            manager.show_student_marks()
        elif choice == "7":
            manager.show_gpa_ranking()
        elif choice == "0":
            show_banner(["Goodbye!"])
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
