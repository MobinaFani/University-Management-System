from .DA import database

class StaffManager:
    def register_staff(self, code, name, family, user, password):
        database.insert_staff(code, name, family, user, password)

    def add_professor(self, code, name, family, user, password):
        self.register_professor(code, name, family, user, password)

    def add_student(self, code, name, family, user, password):
        self.register_student(code, name, family, user, password)

    def add_course(self, code, name, unit):
        self.register_course(code, name, unit)

    def register_student(self, code, name, family, user, password):
        database.insert_student(code, name, family, user, password)

    def register_professor(self, code, name, family, user, password):
        database.insert_professor(code, name, family, user, password)

    def register_course(self, code, name, unit):
        database.insert_course(code, name, unit)

    def assign_course_to_professor(self, course_code, professor_code):
        database.assign_course_to_professor(course_code, professor_code)

    def get_my_info(self, username):
        conn = database.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM staffs WHERE user=?", (username,))
        row = cur.fetchone()
        conn.close()
        if row:
            return {
                'code': row[0],
                'name': row[1],
                'family': row[2],
                'user': row[3],
                'pass': row[4]
            }
        return None


class StudentManager:
    def choose_course(self, student_code, course_code):
        database.assign_course_to_student(student_code, course_code)

    def get_all_courses(self):
        return database.get_courses()

    def get_report(self, student_code):
        try:
            conn = database.connect()
            cur = conn.cursor()
            cur.execute("""
                SELECT c.name, c.unit, a.grade 
                FROM assignments a
                JOIN courses c ON a.course_code = c.code
                WHERE a.student_code=?
                ORDER BY c.name
            """, (student_code,))

            rows = cur.fetchall()
            conn.close()

            if not rows:
                return {'courses': [], 'average': 0.0}

            graded = [r for r in rows if r[2] is not None]
            avg = round(sum(r[1] * r[2] for r in graded) / sum(r[1] for r in graded), 2) if graded else 0.0

            return {
                'courses': rows,
                'average': avg
            }

        except Exception as e:
            print(f"Error in get_report: {e}")
            return {'courses': [], 'average': 0.0}


    def get_my_info(self, username):
        conn = database.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM students WHERE user=?", (username,))
        row = cur.fetchone()
        conn.close()
        if row:
            return {
                'code': row[0],
                'name': row[1],
                'family': row[2],
                'user': row[3],
                'pass': row[4]
            }
        return None


class ProfessorManager:
    def __init__(self, username):
        self.username = username
        self.professor_code = self.get_code_by_username(username)

    def get_professor_code_by_username(self, username):
        conn = database.connect()
        cur = conn.cursor()
        cur.execute("SELECT code FROM professors WHERE user=?", (username,))
        row = cur.fetchone()
        conn.close()
        return row[0] if row else None

    def get_code_by_username(self, username):
        conn = database.connect()
        cur = conn.cursor()
        cur.execute("SELECT code FROM professors WHERE user=?", (username,))
        row = cur.fetchone()
        conn.close()
        return row[0] if row else None

    def give_grade(self, student_code, course_code, grade):
        if not self.username:
            return False

        conn = database.connect()
        cur = conn.cursor()

        cur.execute("""
            SELECT * FROM course_professor 
            WHERE course_code = ? AND professor_code = (
                SELECT code FROM professors WHERE user = ?
            )
        """, (course_code, self.username))
        if not cur.fetchone():
            conn.close()
            return False

        try:
            cur.execute("""
                UPDATE assignments SET grade=? 
                WHERE student_code=? AND course_code=?
            """, (float(grade), student_code, course_code))
            conn.commit()
            return True
        except:
            conn.rollback()
            return False
        finally:
            conn.close()

    def get_course_report(self, course_code):
        conn = database.connect()
        cur = conn.cursor()
        cur.execute('''
            SELECT s.name, s.family, a.grade 
            FROM assignments a
            JOIN students s ON a.student_code = s.code
            JOIN course_professor cp ON a.course_code = cp.course_code
            JOIN professors p ON cp.professor_code = p.code
            WHERE a.course_code = ? AND p.user = ?
        ''', (course_code, self.username))
        data = cur.fetchall()
        conn.close()

        if not data:
            return {'grades': [], 'average': 0, 'top': 'N/A', 'bottom': 'N/A'}

        valid_grades = [r for r in data if r[2] is not None]
        if not valid_grades:
            return {'grades': data, 'average': 0, 'top': 'N/A', 'bottom': 'N/A'}

        average = round(sum(r[2] for r in valid_grades) / len(valid_grades), 2)
        top = max(valid_grades, key=lambda x: x[2])
        bottom = min(valid_grades, key=lambda x: x[2])

        return {
            'grades': data,
            'average': average,
            'top': f"{top[0]} {top[1]}",
            'bottom': f"{bottom[0]} {bottom[1]}"
        }

    def get_my_info(self, username):
        conn = database.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM professors WHERE user=?", (username,))
        row = cur.fetchone()
        conn.close()
        if row:
            return {
                'code': row[0],
                'name': row[1],
                'family': row[2],
                'user': row[3],
                'pass': row[4]
            }
        return None