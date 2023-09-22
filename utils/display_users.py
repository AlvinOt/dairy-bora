from sqlalchemy.orm import sessionmaker
from database.database import engine, Session
from database.models import User

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

def main():
    # Retrieve all users from the database
    users = session.query(User).all()

    # Display user information
    for user in users:
        print(f"User ID: {user.id}")
        print(f"Username: {user.username}")
        print(f"Role: {user.role}")
        print(f"Contact Information: {user.contact_information}")
        print("-" * 30)

if __name__ == "__main__":
    main()
