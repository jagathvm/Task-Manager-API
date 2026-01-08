# Task Management REST API (Python)

A simple **Task Management REST API** built using **Python and Flask**, implementing full CRUD operations for users and tasks with a relational SQL database.

This project demonstrates core backend development concepts such as **REST APIs, Object-Oriented Programming (OOP), SQL databases, and Git version control**.

---

## 🚀 Features

- Create and retrieve users
- Create, retrieve, update, and delete tasks
- Tasks linked to users using foreign key relationships
- Input validation and error handling
- JSON-based API responses
- Clean and modular code structure

---

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** Flask
- **Database:** SQLite (SQL-based, easily portable to MySQL/PostgreSQL)
- **API Testing:** Postman
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

```text
task-manager-api/
│
├── app.py # Flask application and API routes
├── main.py # Database initialization
├── requirements.txt # Python dependencies
├── .gitignore
│
├── database/
│ └── db.py # Database connection and table creation
│
├── models/
│ └── user.py # OOP model classes
│
└── README.md

---

## 🔧 Setup & Run Locally

```

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/task-manager-api.git
cd task-manager-api
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Initialize database

```bash
python main.py
```

### 5️⃣ Run the Flask server

```bash
python app.py
```

Server will start at: http://127.0.0.1:5000

## 📌 API Endpoints

### 👤 Users

| Method | Endpoint | Description       |
| ------ | -------- | ----------------- |
| POST   | `/users` | Create a new user |
| GET    | `/users` | Get all users     |

---

### 📋 Tasks

| Method | Endpoint      | Description                 |
| ------ | ------------- | --------------------------- |
| POST   | `/tasks`      | Create a new task           |
| GET    | `/tasks`      | Get all tasks               |
| PUT    | `/tasks/<id>` | Update task title or status |
| DELETE | `/tasks/<id>` | Delete a task               |
