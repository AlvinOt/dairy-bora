import sys
import os

# Add the project directory to sys.path
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_dir)

from sqlalchemy.orm import sessionmaker
from database_dir.database import engine, Session
from database_dir.models import User
from passlib.hash import bcrypt

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

def main():
    # Create user records
    users_data = [
        {"username": "richomie", "password_hashed": bcrypt.hash("password123"), "role": "treasurer"},
        {"username": "marygerry", "password_hashed": bcrypt.hash("securepass"), "role": "assistantmanager"}
    ]

    for user_data in users_data:
        new_user = User(**user_data)
        session.add(new_user)

    session.commit()

    print("User records added successfully.")

if __name__ == "__main__":
    main()

