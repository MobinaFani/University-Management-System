import sys
import os
sys.path.append(os.path.dirname(__file__))
from staff_form import open_staff_panel
from student_form import open_student_panel
from professor_form import open_professor_panel
from tkinter import *
from tkinter import messagebox
from staff_form import open_staff_panel
from professor_form import open_professor_panel
from student_form import open_student_panel
from BL.DA.database import check_login

def login_window():
    win = Tk()
    win.title("Login - University System")
    win.geometry("300x300")

    Label(win, text="User:").pack()
    ent_user = Entry(win)
    ent_user.pack()

    Label(win, text="Password:").pack()
    ent_pass = Entry(win, show="*")
    ent_pass.pack()

    Label(win, text="Role:").pack()
    role = StringVar()
    role.set("student")
    OptionMenu(win, role, "student", "professor", "staff").pack()

    def login():
        u = ent_user.get()
        p = ent_pass.get()
        r = role.get()

        if check_login(r, u, p):
            if r == "staff":
                open_staff_panel(u)
            elif r == "professor":
                open_professor_panel(u)
            elif r == "student":
                open_student_panel(u)
        else:
            messagebox.showerror("❌ خطا", "نام کاربری یا رمز اشتباه است")

    Button(win, text="Login", command=login).pack(pady=10)
    win.mainloop()