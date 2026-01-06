from flask import Flask, request
from database.db import get_db_connection

app = Flask(__name__)

# Create Home Route (GET /)
@app.route('/')
def home():
  return {"message": "Task Manager API is running !"}

# Create User API (POST /users)
@app.route('/user', methods=["POST"])
def create_user():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")

    # basic validation

    if not name and email:
       return {"error": "Name value is required"}, 400

    if not email and name:
       return {"error": "Email value is required"}, 400

    if not name or not email:
       return {"error": "Name and Email values are required"}, 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
      cursor.execute(
         "INSERT INTO users (name, email) VALUES (?, ?)",
         (name, email)
      )
      conn.commit()

      return {"message": "User created successfully"}, 201

    except Exception as e:
       return {"error": str(e)}, 500

    finally:
       conn.close()

# POST -	send data to server
# request.get_json() -	read JSON body
# SQL INSERT	- add record into table
# validation	- check user input
# HTTP codes	- 201 success, 400 bad input
# try–except	- error handling
# finally	- always closes DB

# Get all users (GET /users)
@app.route('/users', methods=["GET"])
def get_users():
   conn = get_db_connection()
   cursor = conn.cursor()

   cursor.execute("SELECT id, name, email FROM users")
   rows = cursor.fetchall()

   users = []

   for row in rows:
      users.append({
         "id": row["id"],
         "name": row["name"],
         "email": row["email"]
      })

   conn.close()

   return {"users": users}, 200

# methods=["GET"] - Only accepts GET requests
# cursor.execute() -	runs SQL query
# fetchall() -	returns all rows
# for row in rows -	loop through SQL rows
# row["name"]	- dictionary-like access
# return {"users": users} -	send JSON response

# Create Task API (POST /tasks)
@app.route("/task", methods=["POST"])
def create_task():
   data = request.get_json()

   user_id = data.get("user_id")
   title = data.get("title")
   status = data.get("status", "pending")   #  default value

   # validation
   if not user_id and title:
      return {"error": "user_id is required"}, 400

   if user_id and not title:
      return {"error": "title is required"}, 400

   if not user_id or not title:
      return {"error": "user_id and title are required"}, 400

   conn = get_db_connection()
   cursor = conn.cursor()

   #  check if user exists
   cursor.execute("SELECT id FROM users WHERE id = ?", (user_id,))
   user = cursor.fetchone()

   if not user:
      conn.close()
      return {"error": "User does not exist"}, 404

   try:
      cursor.execute(
         "INSERT INTO tasks (user_id, title, status) VALUES (?, ?, ?)",
         (user_id, title, status)
      )
      conn.commit()

      return {"message": "Task created successfully"}, 201

   except Exception as e:
      return {"error": str(e)}, 500

   finally:
      conn.close()

# Foreign key check	- Ensures task belongs to valid user
# Default status - "pending" when not sent
# Validation	- input checking
# SQL insert	- into tasks table
# 404 Not Found -	resource missing
# 500	- server / DB errors

# Get all tasks (GET /tasks)
@app.route('/tasks', methods=["GET"])
def get_tasks():
   conn = get_db_connection()
   cursor = conn.cursor()

   cursor.execute("SELECT id, user_id, title, status FROM tasks")
   rows = cursor.fetchall()

   tasks = []

   for row in rows:
      tasks.append({
         "id": row["id"],
         "user_id": row["user_id"],
         "title": row["title"],
         "status": row["status"]
      })

   conn.close()

   return {"tasks": tasks}, 200

# Update a task (PUT /tasks/<id>)
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
   data = request.get_json()

   title = data.get("title")
   status = data.get("status")

  # at least one field should be provided
   if not title and not status:
      return {"error": "Nothing to update. Provide title or status."}, 400

   conn = get_db_connection()
   cursor = conn.cursor()

   cursor.execute("SELECT id FROM tasks WHERE id = ?", (task_id,))
   task = cursor.fetchone()

   if not task:
      conn.close()
      return {"error": "Task not found"}, 404

  #  prepare dynamic update query
   updates = []
   params = []

   if title:
      updates.append("title = ?")
      params.append(title)

   if status:
      updates.append("status = ?")
      params.append(status)

   params.append(task_id)

   cursor.execute(f"UPDATE tasks SET {', '.join(updates)} WHERE id = ?", params)
   conn.commit()
   conn.close()

   return {"message": "Task updated successfully"}, 200

# SQL UPDATE tasks	- update task inside tasks table

if __name__ == "__main__":
  app.run(debug=True)
