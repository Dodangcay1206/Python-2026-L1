import sys

try:
    import curses
except ImportError:  
    curses = None

def _draw_banner(stdscr, lines):
    curses.curs_set(0)
    stdscr.clear()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    height, width = stdscr.getmaxyx()
    box_height = min(len(lines) + 4, height)
    box_width = min(max(len(line) for line in lines) + 6, width)
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

def list_students(students):
    print("\n--- Student List ---")
    if not students:
        print("No students available.")
        return
    for student in students:
        print(student)

def list_courses(courses):
    print("\n--- Course List ---")
    if not courses:
        print("No courses available.")
        return
    for course in courses:
        print(course)

def show_marks_for_course(course_id, students, marks):
    print(f"\n--- Marks for course {course_id} ---")
    course_marks = marks.get(course_id, {})
    for student in students:
        s_id = student.student_id
        if s_id in course_marks:
            print(f"ID: {s_id} - Name: {student.name} - Mark: {course_marks[s_id]}")
        else:
            print(f"ID: {s_id} - Name: {student.name} - Mark: (not entered)")

def show_gpa_ranking(ranking):
    if not ranking:
        print("No student has marks yet.")
        return
    print("\n--- GPA Ranking (descending) ---")
    for rank, (student, gpa) in enumerate(ranking, start=1):
        print(f"{rank}. {student.name} (ID: {student.student_id}) - GPA: {gpa:.2f}")