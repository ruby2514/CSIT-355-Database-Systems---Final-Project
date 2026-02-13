import sqlite3
import sys

DB_PATH = "university.db"

def get_connection(path=DB_PATH):
    return sqlite3.connect(path)

def create_tables(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            course_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            credits INTEGER NOT NULL
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS enrollment (
            enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            course_id TEXT NOT NULL,
            FOREIGN KEY(student_id) REFERENCES students(student_id) ON DELETE CASCADE,
            FOREIGN KEY(course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
            UNIQUE(student_id, course_id)
        );
    """)
    # Sample data insertion (only if tables were just created and are empty)
    cur.execute("INSERT OR IGNORE INTO students(student_id, name, email) VALUES (?, ?, ?)", (1001, 'Alice Johnson', 'johnsona3@montclair.edu'))
    cur.execute("INSERT OR IGNORE INTO students(student_id, name, email) VALUES (?, ?, ?)", (1002, 'Bob Lee', 'leeb1@montclair.edu'))
    cur.execute("INSERT OR IGNORE INTO students(student_id, name, email) VALUES (?, ?, ?)", (1003, 'Carlos Mendez', 'mendezc5@montclair.edu'))
    cur.execute("INSERT OR IGNORE INTO students(student_id, name, email) VALUES (?, ?, ?)", (1004, 'Diana Smith', 'smithd2@montclair.edu'))
    cur.execute("INSERT OR IGNORE INTO students(student_id, name, email) VALUES (?, ?, ?)", (1005, 'Eve Chen', 'chene1@montclair.edu'))

    cur.execute("INSERT OR IGNORE INTO courses(course_id, name, credits) VALUES (?, ?, ?)", ('CSIT355', 'Database System', 3))
    cur.execute("INSERT OR IGNORE INTO courses(course_id, name, credits) VALUES (?, ?, ?)", ('CSIT337', 'Internet Computing', 3))
    cur.execute("INSERT OR IGNORE INTO courses(course_id, name, credits) VALUES (?, ?, ?)", ('AMAT345', 'Applied Probability', 3))
    cur.execute("INSERT OR IGNORE INTO courses(course_id, name, credits) VALUES (?, ?, ?)", ('AMAT120', 'Calculus A', 4))
    cur.execute("INSERT OR IGNORE INTO courses(course_id, name, credits) VALUES (?, ?, ?)", ('PEGN278', 'Yoga', 1))

    cur.execute("INSERT OR IGNORE INTO enrollment(student_id, course_id) VALUES (?, ?)", (1001, 'CSIT355'))
    cur.execute("INSERT OR IGNORE INTO enrollment(student_id, course_id) VALUES (?, ?)", (1001, 'CSIT337'))
    cur.execute("INSERT OR IGNORE INTO enrollment(student_id, course_id) VALUES (?, ?)", (1002, 'CSIT355'))
    cur.execute("INSERT OR IGNORE INTO enrollment(student_id, course_id) VALUES (?, ?)", (1002, 'AMAT345'))
    cur.execute("INSERT OR IGNORE INTO enrollment(student_id, course_id) VALUES (?, ?)", (1003, 'AMAT120'))
    cur.execute("INSERT OR IGNORE INTO enrollment(student_id, course_id) VALUES (?, ?)", (1003, 'PEGN278'))
    cur.execute("INSERT OR IGNORE INTO enrollment(student_id, course_id) VALUES (?, ?)", (1004, 'CSIT355'))
    cur.execute("INSERT OR IGNORE INTO enrollment(student_id, course_id) VALUES (?, ?)", (1004, 'PEGN278'))
    cur.execute("INSERT OR IGNORE INTO enrollment(student_id, course_id) VALUES (?, ?)", (1005, 'AMAT345'))
    cur.execute("INSERT OR IGNORE INTO enrollment(student_id, course_id) VALUES (?, ?)", (1005, 'AMAT120'))
    conn.commit()

def input_nonempty(prompt):
    while True:
        v = input(prompt).strip()
        if v:
            return v

def start():
    print("Welcome to the University Enrollment App")
    conn = get_connection()
    create_tables(conn) # Call create_tables here
    try:
        while True:
            sid_input = input("Enter student ID (or -1 to create a new student, X to exit): ").strip()
            if sid_input.upper() == 'X':
                print("Goodbye!")
                return
            if sid_input == '-1':
                sid = create_new_student(conn)
            else:
                if not sid_input.isdigit():
                    print("Student ID must be a number or -1.")
                    continue
                sid = int(sid_input)
                if not student_exists(conn, sid):
                    print(f"Student ID {sid} not found. Enter -1 to create a new student.")
                    continue
            student_menu(conn, sid)
    finally:
        conn.close()

# --- DB helper functions ---

def student_exists(conn, sid):
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM students WHERE student_id = ?", (sid,))
    return cur.fetchone() is not None

def create_new_student(conn):
    cur = conn.cursor()
    print("Create New Student")
    while True:
        sid_input = input_nonempty("New student ID (integer): ")
        if not sid_input.isdigit():
            print("Student ID must be numeric.")
            continue
        sid = int(sid_input)
        if student_exists(conn, sid):
            print("This student ID already exists. Pick another.")
            continue
        break
    name = input_nonempty("Student full name: ")
    email = input_nonempty("Email: ")
    cur.execute("INSERT INTO students(student_id, name, email) VALUES(?, ?, ?)", (sid, name, email))
    conn.commit()
    print(f"Student {name} (ID {sid}) created.")
    return sid

# --- Menu functions ---

def student_menu(conn, sid):
    print(f"\nActive student ID: {sid}\n")
    while True:
        print("Student Menu:")
        print("L - List courses")
        print("E - Enroll in a course")
        print("W - Withdraw from a course")
        print("S - Search courses by name substring")
        print("M - My Classes")
        print("X - Exit to main")
        choice = input("Enter option: ").strip().upper()
        if choice == 'L':
            list_courses(conn)
        elif choice == 'E':
            enroll_course(conn, sid)
        elif choice == 'W':
            withdraw_course(conn, sid)
        elif choice == 'S':
            search_courses(conn)
        elif choice == 'M':
            list_my_classes(conn, sid)
        elif choice == 'X':
            print("Returning to main...")
            break
        else:
            print("Unknown option. Please enter one of L, E, W, S, M, X.")

def list_courses(conn):
    cur = conn.cursor()
    cur.execute("SELECT course_id, name, credits FROM courses ORDER BY course_id")
    rows = cur.fetchall()
    if not rows:
        print("No courses found.")
        return
    print("Courses:")
    for r in rows:
        print(f"{r[0]} | {r[1]} | {r[2]} credits")

def enroll_course(conn, sid):
    cur = conn.cursor()
    course_id = input_nonempty("Enter course ID to enroll: ")
    # ensure course exists
    cur.execute("SELECT 1 FROM courses WHERE course_id = ?", (course_id,))
    if cur.fetchone() is None:
        print(f"Course {course_id} does not exist.")
        return
    # conflict check
    cur.execute("SELECT 1 FROM enrollment WHERE student_id = ? AND course_id = ?", (sid, course_id))
    if cur.fetchone() is not None:
        print("You are already enrolled in this course.")
        return
    cur.execute("INSERT INTO enrollment(student_id, course_id) VALUES(?, ?)", (sid, course_id))
    conn.commit()
    print(f"Enrolled student {sid} in course {course_id}.")

def withdraw_course(conn, sid):
    cur = conn.cursor()
    course_id = input_nonempty("Enter course ID to withdraw from: ")
    cur.execute("SELECT 1 FROM enrollment WHERE student_id = ? AND course_id = ?", (sid, course_id))
    if cur.fetchone() is None:
        print("Enrollment record not found.")
        return
    cur.execute("DELETE FROM enrollment WHERE student_id = ? AND course_id = ?", (sid, course_id))
    conn.commit()
    print(f"Withdrawn student {sid} from course {course_id}.")

def search_courses(conn):
    cur = conn.cursor()
    substr = input_nonempty("Enter substring to search in course names: ")
    pattern = f"%{substr}%"
    cur.execute("SELECT course_id, name, credits FROM courses WHERE name LIKE ? COLLATE NOCASE", (pattern,))
    rows = cur.fetchall()
    if not rows:
        print("No matching courses.")
        return
    print("Matching courses:")
    for r in rows:
        print(f"{r[0]} | {r[1]} | {r[2]} credits")

def list_my_classes(conn, sid):
    cur = conn.cursor()
    cur.execute(
        "SELECT c.course_id, c.name, c.credits FROM courses c JOIN enrollment e ON c.course_id = e.course_id WHERE e.student_id = ?",
        (sid,)
    )
    rows = cur.fetchall()
    if not rows:
        print("You are not enrolled in any courses.")
        return
    print("My Classes:")
    for r in rows:
        print(f"{r[0]} | {r[1]} | {r[2]} credits")

if __name__ == '__main__':
    start()
