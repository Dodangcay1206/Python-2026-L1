import numpy as np
import input as student_input 
import output as student_output

students = []  
courses = []    
marks = {}     

def find_course(course_id):
    for course in courses:
        if course.course_id == course_id:
            return course
    return None

def calculate_gpa(student_id):
    credits = []
    student_marks = []
    for course in courses:
        course_marks = marks.get(course.course_id, {})
        if student_id in course_marks:
            credits.append(course.credit)
            student_marks.append(course_marks[student_id])
    if not credits:
        return None
    credits_arr = np.array(credits, dtype=float)
    marks_arr = np.array(student_marks, dtype=float)
    gpa = np.sum(credits_arr * marks_arr) / np.sum(credits_arr)
    return float(gpa)

def build_gpa_ranking():
    ranking = []
    for student in students:
        gpa = calculate_gpa(student.student_id)
        if gpa is not None:
            ranking.append((student, gpa))
    ranking.sort(key=lambda pair: pair[1], reverse=True)
    return ranking

def action_input_students(): 
    students.extend(student_input.input_student_info())

def action_input_courses():
    courses.extend(student_input.input_course_info())

def action_input_marks():
    if not courses:
        print("Please add courses first!")
        return
    if not students:
        print("Please add students first!")
        return
    student_output.list_courses(courses)
    course_id = student_input.input_course_id("\nEnter course ID to give marks: ")
    if find_course(course_id) is None:
        print("Course ID not found!")
        return
    course_marks = marks.setdefault(course_id, {})
    for student in students:
        course_marks[student.student_id] = student_input.input_mark_for(student)

def action_show_marks():
    if not marks:
        print("No marks entered yet.")
        return
    student_output.list_courses(courses)
    course_id = student_input.input_course_id("\nEnter course ID to view marks: ")
    if course_id not in marks:
        print("No marks found for this course ID.")
        return
    student_output.show_marks_for_course(course_id, students, marks)

def action_show_gpa_ranking():
    if not students:
        print("No students available.")
        return
    student_output.show_gpa_ranking(build_gpa_ranking())

def main():
    student_output.show_banner(
        ["STUDENT MARK MANAGEMENT", "Practical Work 4", "Press any key to start"]
    )

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
            action_input_students()
        elif choice == "2":
            action_input_courses()
        elif choice == "3":
            action_input_marks()
        elif choice == "4":
            student_output.list_courses(courses)
        elif choice == "5":
            student_output.list_students(students)
        elif choice == "6":
            action_show_marks()
        elif choice == "7":
            action_show_gpa_ranking()
        elif choice == "0":
            student_output.show_banner(["Goodbye!"])
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()