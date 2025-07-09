import sqlite3

def connect():
    return sqlite3.connect("university.db")

def create_tables():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS students (
        code TEXT PRIMARY KEY, name TEXT, family TEXT, user TEXT, pass TEXT)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS professors (
        code TEXT PRIMARY KEY, name TEXT, family TEXT, user TEXT, pass TEXT)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS staffs (
        code TEXT PRIMARY KEY, name TEXT, family TEXT, user TEXT, pass TEXT)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS courses (
        code TEXT PRIMARY KEY, name TEXT, unit INTEGER)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS course_professor (
        course_code TEXT, professor_code TEXT)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS assignments (
        student_code TEXT,
        course_code TEXT,
        grade REAL,
       PRIMARY KEY (student_code, course_code)
    )""")
    conn.commit()
    conn.close()

def insert_student(code, name, family, user, password):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", (code, name, family, user, password))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.close()

def insert_professor(code, name, family, user, password):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO professors VALUES (?, ?, ?, ?, ?)", (code, name, family, user, password))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.close()

def insert_staff(code, name, family, user, password):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO staffs VALUES (?, ?, ?, ?, ?)", (code, name, family, user, password))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.close()

def insert_course(code, name, unit):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO courses VALUES (?, ?, ?)", (code, name, unit))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.close()

def assign_course_to_professor(course_code, professor_code):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO course_professor VALUES (?, ?)", (course_code, professor_code))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.close()

def assign_course_to_student(student_code, course_code):
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM assignments WHERE student_code=? AND course_code=?", (student_code, course_code))
        if cur.fetchone() is None:
            cur.execute("INSERT INTO assignments(student_code, course_code, grade) VALUES (?, ?, NULL)", (student_code, course_code))
            conn.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.close()

def update_grade(student_code, course_code, grade):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE assignments SET grade = ? WHERE student_code = ? AND course_code = ?", (grade, student_code, course_code))
    conn.commit()
    conn.close()

def get_courses():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM courses")
    rows = cur.fetchall()
    conn.close()
    return rows

def check_login(role, username, password):
    conn = connect()
    cur = conn.cursor()
    table = ""
    if role == "student":
        table = "students"
    elif role == "professor":
        table = "professors"
    elif role == "staff":
        table = "staffs"
    else:
        return False
    cur.execute(f"SELECT * FROM {table} WHERE user=? AND pass=?", (username, password))
    row = cur.fetchone()
    conn.close()
    return row is not None

def insert_default_users():
    try:
        insert_staff("100", "Ahmad", "Karimi", "admin", "1234")
        insert_professor("200", "Zeynab", "Kamali", "prof", "1234")
        insert_student("300", "Mobina", "Fani", "mobina", "1234")
    except:
        pass