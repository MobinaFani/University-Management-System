import sys
import os
from tkinter import messagebox

sys.path.append(os.path.join(os.path.dirname(__file__),"bl"))
from tkinter import *
from BL.logic import ProfessorManager
from BL.DA import database

def open_professor_panel(username):
    win = Tk()
    win.title("پنل استاد")
    win.geometry("500x550")

    pm = ProfessorManager(username)

    lst = Listbox(win, width=60)
    lst.pack()

    list = Listbox(win, width=40)
    list.pack()

    Label(win, text="کد درس:").pack()
    ent_course_code = Entry(win)
    ent_course_code.pack()

    Label(win, text="کد دانشجو:").pack()
    ent_student_code = Entry(win)
    ent_student_code.pack()

    Label(win, text="نمره:").pack()
    ent_grade = Entry(win)
    ent_grade.pack()

    def give_grade():
        success = pm.give_grade(ent_student_code.get(), ent_course_code.get(), float(ent_grade.get()))
        if success:
            list.insert(END, "✅ نمره ثبت شد.")
        else:
            list.insert(END, "❌ شما مجاز نیستید برای این درس نمره ثبت کنید.")

    Button(win, text="ثبت نمره", command=give_grade).pack(pady=5)

    def show_grades():
        course_code = ent_course_code.get()
        if not course_code:
            messagebox.showerror("خطا", "لطفاً کد درس را وارد کنید")
            return

        result = pm.get_course_report(course_code)
        lst.delete(0, END)

        if not result['grades']:
            lst.insert(END, "نمره‌ای برای این درس ثبت نشده است")
            return

        for name, family, grade in result['grades']:
            lst.insert(END, f"{name} {family}: {grade if grade is not None else 'ثبت نشده'}")

        lst.insert(END, "------------------------")
        lst.insert(END, f" معدل کلاس: {result['average']:.2f}")
        lst.insert(END, f" شاگرد اول: {result['top']}")
        lst.insert(END, f" شاگرد آخر: {result['bottom']}")

    Button(win, text="گزارش نمرات", command=show_grades).pack()

    def show_info():
        info = pm.get_my_info(username)
        if info:
          lst.delete(0, END)
          lst.insert(END, f"کد: {info['code']}")
          lst.insert(END, f"نام: {info['name']}")
          lst.insert(END, f"نام خانوادگی: {info['family']}")
          lst.insert(END, f"user: {info['user']}")
          lst.insert(END, f"pass: {info['pass']}")
        else:
            lst.insert(END, "اطلاعاتی یافت نشد")

    Button(win, text="نمایش اطلاعات من", command=show_info).pack()

    win.mainloop()