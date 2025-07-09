import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"bl"))
from tkinter import *
from BL.logic import StaffManager
from tkinter import messagebox

def open_staff_panel(username):
    win = Tk()
    win.title("پنل کارمند")
    win.geometry("500x600")

    canvas = Canvas(win)
    scrollbar = Scrollbar(win, orient=VERTICAL, command=canvas.yview)
    scrollable_frame = Frame(canvas)
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    staff_manager = StaffManager()

    Label(scrollable_frame, text="-- ثبت استاد --", fg="blue").pack(pady=5)
    Label(scrollable_frame, text="کد استاد:").pack()
    prof_code = Entry(scrollable_frame)
    prof_code.pack()
    Label(scrollable_frame, text="نام:").pack()
    prof_name = Entry(scrollable_frame)
    prof_name.pack()
    Label(scrollable_frame, text="نام خانوادگی:").pack()
    prof_family = Entry(scrollable_frame)
    prof_family.pack()
    Label(scrollable_frame, text="نام کاربری:").pack()
    prof_user = Entry(scrollable_frame)
    prof_user.pack()
    Label(scrollable_frame, text="رمز عبور:").pack()
    prof_pass = Entry(scrollable_frame, show="*")
    prof_pass.pack()

    def add_professor():
        staff_manager.add_professor(prof_code.get(), prof_name.get(), prof_family.get(), prof_user.get(), prof_pass.get())
        messagebox.showinfo("موفق", "استاد ثبت شد")

    Button(scrollable_frame, text="ثبت استاد", command=add_professor).pack(pady=10)

    Label(scrollable_frame, text="-- ثبت دانشجو --", fg="blue").pack(pady=5)
    Label(scrollable_frame, text="کد دانشجو:").pack()
    stu_code = Entry(scrollable_frame)
    stu_code.pack()
    Label(scrollable_frame, text="نام:").pack()
    stu_name = Entry(scrollable_frame)
    stu_name.pack()
    Label(scrollable_frame, text="نام خانوادگی:").pack()
    stu_family = Entry(scrollable_frame)
    stu_family.pack()
    Label(scrollable_frame, text="نام کاربری:").pack()
    stu_user = Entry(scrollable_frame)
    stu_user.pack()
    Label(scrollable_frame, text="رمز عبور:").pack()
    stu_pass = Entry(scrollable_frame, show="*")
    stu_pass.pack()

    def add_student():
        staff_manager.add_student(stu_code.get(), stu_name.get(), stu_family.get(), stu_user.get(), stu_pass.get())
        messagebox.showinfo("موفق", "دانشجو ثبت شد")

    Button(scrollable_frame, text="ثبت دانشجو", command=add_student).pack(pady=10)

    Label(scrollable_frame, text="-- ثبت درس --", fg="blue").pack(pady=5)
    Label(scrollable_frame, text="کد درس:").pack()
    course_code = Entry(scrollable_frame)
    course_code.pack()
    Label(scrollable_frame, text="نام درس:").pack()
    course_name = Entry(scrollable_frame)
    course_name.pack()
    Label(scrollable_frame, text="تعداد واحد:").pack()
    course_unit = Entry(scrollable_frame)
    course_unit.pack()

    def add_course():
        staff_manager.add_course(course_code.get(), course_name.get(), course_unit.get())
        messagebox.showinfo("موفق", "درس ثبت شد")

    Button(scrollable_frame, text="ثبت درس", command=add_course).pack(pady=10)

    Label(scrollable_frame, text="-- تخصیص درس به استاد --", fg="blue").pack(pady=5)
    Label(scrollable_frame, text="کد درس:").pack()
    assign_course_code = Entry(scrollable_frame)
    assign_course_code.pack()
    Label(scrollable_frame, text="کد استاد:").pack()
    assign_prof_code = Entry(scrollable_frame)
    assign_prof_code.pack()

    def assign_course():
        staff_manager.assign_course_to_professor(assign_course_code.get(), assign_prof_code.get())
        messagebox.showinfo("موفق", "تخصیص انجام شد")

    Button(scrollable_frame, text="تخصیص درس", command=assign_course).pack(pady=10)

    Label(scrollable_frame, text="-- اطلاعات من --", fg="blue").pack(pady=5)
    info_box = Listbox(scrollable_frame, width=40, height=5)
    info_box.pack()


    def show_info():
        staff = staff_manager.get_my_info(username)
        if staff:
          info_box.delete(0, END)
          info_box.insert(END, "کد: " + staff['code'])
          info_box.insert(END, "نام: " + staff['name'])
          info_box.insert(END, "نام خانوادگی: " + staff['family'])
          info_box.insert(END, "نام کاربری: " + staff['user'])
          info_box.insert(END, "رمز عبور: " + staff['pass'])
        else:
            info_box.insert(END, "اطلاعاتی یافت نشد")


    Button(scrollable_frame, text="نمایش اطلاعات من", command=show_info, bg="lightgray").pack(pady=10)

    win.mainloop()
