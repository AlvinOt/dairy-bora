import sys
import os

# Add the project directory to sys.path
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_dir)

from sqlalchemy.orm import sessionmaker
from database_dir.database import engine, Session
from database_dir.models import User

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

def main():
    # Retrieve the user to update
    user_to_update = session.query(User).filter_by(username="richard").first()

    if user_to_update:
        # Update the contact information
        new_contact_information = "richjuma.com"
        user_to_update.contact_information = new_contact_information

        # Commit the changes to the database
        session.commit()

        print("Contact information updated successfully.")
    else:
        print("User not found.")

if __name__ == "__main__":
    main()

