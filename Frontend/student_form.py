import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"bl"))
from BL.logic import StudentManager
from BL.DA import database
from tkinter import *
from tkinter import messagebox
sm = StudentManager()

def open_student_panel(username):
    conn = database.connect()
    cur = conn.cursor()
    cur.execute("SELECT code FROM students WHERE user=?", (username,))
    row = cur.fetchone()
    conn.close()
    if row:
        student_code = row[0]
    else:
        messagebox.showerror("خطا", "کد دانشجویی یافت نشد")
        return

    win = Tk()
    win.title("پنل دانشجو")
    win.geometry("500x550")

    global lbx_courses
    lbx_courses = Listbox(win)
    lbx_courses.pack()

    global lbx_report
    lbx_report = Listbox(win, width=50)
    lbx_report.pack()

    def load_courses():
        lbx_courses.delete(0, END)
        for row in sm.get_all_courses():
            lbx_courses.insert(END, row[0] + " - " + row[1] + f" ({row[2]} واحد)")

    def choose_course():
        selected = lbx_courses.curselection()
        if not selected:
            messagebox.showwarning("هشدار", "لطفاً یک درس را از لیست انتخاب کنید.")
            return

        course_info = lbx_courses.get(selected[0])

        try:
            course_code = course_info.split("-")[0].strip()
            sm.choose_course(student_code, course_code)
            messagebox.showinfo("موفق", f"درس با کد {course_code} انتخاب شد.")
        except Exception as e:
            messagebox.showerror("خطا", f"در هنگام انتخاب واحد مشکلی پیش آمد:\n{e}")

    Button(win, text="نمایش دروس", command=load_courses).pack()
    Button(win, text="انتخاب واحد", command=choose_course).pack()

    def show_report():
        result = sm.get_report(student_code)
        lbx_report.delete(0, END)
        for row in result['courses']:
            lbx_report.insert(END, f"{row[0]} - واحد: {row[1]} - نمره: {row[2]}")
        lbx_report.insert(END, "------------------")
        lbx_report.insert(END, f"معدل کل: {result['average']}")

    Button(win, text="نمایش کارنامه", command=show_report).pack()

    def show_my_info():
        info = sm.get_my_info(username)
        if info:
          lbx_courses.delete(0, END)
          lbx_courses.insert(END, f"کد: {info['code']}")
          lbx_courses.insert(END, f"نام: {info['name']}")
          lbx_courses.insert(END, f"نام خانوادگی: {info['family']}")
          lbx_courses.insert(END, f"user: {info['user']}")
          lbx_courses.insert(END, f"pass: {info['pass']}")
        else:
            lbx_courses.insert(END,"اطلاعاتی یافت نشد")

    Button(win, text="نمایش اطلاعات من", command=show_my_info).pack(pady=5)

    win.mainloop()