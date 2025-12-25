# Start Flask REST API
# Create User API (POST /users)
from flask import Flask, request

from database.db import get_db_connection

app = Flask(__name__)

@app.route('/')
def home():
  return {"message": "Task Manager API is running !"}

@app.route('/users', methods=["POST"])
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

if __name__ == "__main__":
  app.run(debug=True)
