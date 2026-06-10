<div align="center">

# 🎓 Student Marks Management System

A lightweight, terminal-based academic management tool for administrators and teachers —
featuring secure role-based access, automated grading, and exportable performance reports.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/Storage-JSON-F7DF1E?style=flat-square&logo=json&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

</div>

---

## ✨ Features

| Feature                  | Description                                                               |
| ------------------------ | ------------------------------------------------------------------------- |
| 🔒 **Multi-Role Auth**   | Role-based access control separating Admin and Teacher capabilities       |
| 📂 **JSON Data Storage** | Lightweight file-based backend — no database setup required               |
| 📈 **Automated Grading** | Instant totals, percentages, pass/fail status, GPA, and letter grades     |
| 📥 **CSV Export**        | One-click generation of structured, spreadsheet-ready performance reports |

---

## 🏗️ System Architecture

The system uses a structured JSON layout to organise all academic data:

```text
db/
├── students.json        # Student profiles and roll numbers
├── subjects.json        # Subject registry
└── marks.json           # Assessment records linked by student & subject ID
```

### Data Schema

```json
// students.json
[
  {
    "userId": 1,
    "username": "JaneDaneUsername",
    "name": "Jane Dane",
    "password": "123",
    "role": "Student"
  }
]
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- `pip` package manager

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Cakwei/SMMS.git
cd SMMS

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python main.py
```

---

## 👤 Roles & Access

| Role        | Permissions                                  |
| ----------- | -------------------------------------------- |
| **Admin**   | Manage students, subjects, and user accounts |
| **Teacher** | Input marks, view reports, export CSV        |
| **Student** | View results, export CSV                     |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">
Made by Cakwei with ❤️
</div>
