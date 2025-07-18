# 🧑‍💼 Client Dashboard

A full-featured Flask-based admin dashboard that supports user registration, login, session management, and CRUD operations for user management. Includes role-based access control (admin-only pages), and uses Bootstrap for responsive UI.

---

## 🚀 Features

- User Registration & Login (with password hashing)
- Admin Panel with Dashboard overview
- User Roles: Admin, Editor, Viewer
- Role-based Access Control
- CRUD Operations for Users (Create, Read, Update, Delete)
- Session management (login/logout)
- Flash messaging for user feedback
- Responsive UI with Bootstrap 5
- SQLite as the database

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, Bootstrap 5, Jinja2
- **Database**: SQLite
- **Security**: Werkzeug (password hashing), Flask sessions

---

## 📁 Folder Structure

dashboard/
│
├── app.py # Main Flask app
├── auth.py # Authentication & user management logic
├── init_db.py # Script to initialize SQLite DB
├── users.db # SQLite database (generated after first run)
├── templates/ # Jinja2 templates
│ ├── layout.html
│ ├── login.html
│ ├── register.html
│ ├── dashboard.html
│ ├── users.html
│ ├── add_user.html
│ ├── edit_user.html
│ ├── access_denied.html
│ ├── profile.html
│ ├── settings.html
│ └── reports.html
│
├── static/
│ └── style.css # Custom styles
│
├── requirements.txt # Python dependencies
└── README.md

---

✅ Getting Started
1. Clone the Repository:
   git clone https://github.com/yourusername/dashboard.git
   cd dashboard

2. Create and Activate Virtual Environment:
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On macOS/Linux

3. Install Dependencies:
   pip install -r requirements.txt

4. Initialize the Database:
   python init_db.py

5. Run the App:
   python app.py
   
   Visit http://127.0.0.1:5000
   
🔐 Admin Access
- First registered user becomes Admin.
- Admin can:
  - View all users
  - Add/edit/delete users
  - Access admin-only pages
  - 
📄 License
This project is for educational and portfolio purposes only.

✍️ Author
Stanislav Vasilkovski
GitHub: https://github.com/vasilkovskis

