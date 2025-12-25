# Initialize database and create tables

from database.db import create_tables

if __name__ == "__main__":
  create_tables()
  print("Database and tables successfully.")
