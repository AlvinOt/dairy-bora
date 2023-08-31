# scripts/main_users.py

from sqlalchemy.orm import sessionmaker
from database.database import engine, Session
from database.models import User
from passlib.hash import bcrypt

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

def main():
    # Create user records
    users_data = [
        {"username": "richard", "password_hashed": bcrypt.hash("password123"), "role": "farmer"},
        {"username": "maryg", "password_hashed": bcrypt.hash("securepass"), "role": "manager"}
    ]

    for user_data in users_data:
        new_user = User(**user_data)
        session.add(new_user)

    session.commit()

    print("User records added successfully.")

if __name__ == "__main__":
    main()

