import sys
import os
sys.path.append(os.path.dirname(__file__))

from BL.DA import database
from login_form import login_window

database.create_tables()
database.insert_default_users()

def ensure_default_users():
    conn = database.connect()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM students")
    student_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM professors")
    prof_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM staffs")
    staff_count = cur.fetchone()[0]

    if student_count == 0:
        database.insert_student("300", "Mobina", "Fani", "mobina", "1234")

    if prof_count == 0:
        database.insert_professor("200", "Zeynab", "Kamali", "prof", "1234")

    if staff_count == 0:
        database.insert_staff("100", "Ahmad", "Karimi", "admin", "1234")

    conn.close()

ensure_default_users()

login_window()
