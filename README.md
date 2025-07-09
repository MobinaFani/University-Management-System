
# 🎓 University Management System

A Python-based desktop application simulating a basic university system using **Object-Oriented Programming (OOP)**, **Tkinter GUI**, and **SQLite database**.

This project follows a clean **three-layer architecture**:
- **Frontend**: User interfaces with Tkinter
- **Business Logic (BL)**: Core logic and rules of the system
- **Data Access (DA)**: Database interaction using SQLite

---

## ✅ Features

### 👩‍🎓 Student
- Login
- Course selection (unit picking)
- View transcript with GPA
- View personal information

### 👨‍🏫 Professor
- Login
- Assign grades to students
- View class report (top student, GPA)
- View personal information

### 👨‍💼 Employee
- Login
- Add/edit: students, professors, courses
- Assign courses to professors
- View personal information

---

## 🧠 Technologies Used

- Python 3
- Tkinter for GUI
- SQLite for local database
- OOP for clean logic structure

---

## 🗂️ Project Structure

```
UniversitySystemProject/
├── frontend/
│   ├── student_form.py
│   ├── professor_form.py
│   ├── staff_form.py
│   ├── login_form.py
│
├── BL/
│   ├── logic.py
│   └── DA/
│       └── database.py
│
├── main.py
└── README.md
```

---

## 🚀 How to Run

Make sure all files are in the correct structure.

```bash
python main.py
```

---

## 👩🏻‍💻 Author

Mobina Fani  
Python & GUI Developer | Passionate about clean code and learning

---

## 📎 License

This project is provided for academic and educational use only.
