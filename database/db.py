# Database connection and table creation

import sqlite3

DB_NAME = "task_manager.db"

def get_db_connection():
  conn = sqlite3.connect(DB_NAME)
  conn.row_factory = sqlite3.Row
  return conn

def create_tables():
  conn = get_db_connection()
  cursor = conn.cursor()

  # create users table
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
        )
    """)

  # create tasks table
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT NOT NULL,
        status TEXT DEFAULT 'pending',
        FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)

  conn.commit()
  conn.close()
