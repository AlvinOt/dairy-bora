from sqlalchemy.orm import sessionmaker
from database_dir.models import Animal
from sqlalchemy import create_engine

# Define your database connection URL
DB_URL = 'mysql+mysqlconnector://farmanager:manage123@localhost/farmgt'

# Create a database engine
engine = create_engine(DB_URL)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

def main():
    try:
        # Retrieve all animals from the database
        animals = session.query(Animal).all()

        # Display animal information
        for animal in animals:
            print(f"Animal ID: {animal.id}")
            print(f"Name: {animal.name}")
            print(f"Breed: {animal.breed}")
            print(f"Birth Date: {animal.birth_date}")
            print(f"Gender: {animal.gender}")
            print(f"Health Information: {animal.health_information}")
            print(f"Reproductive Status: {animal.reproductive_status}")
            print("-" * 30)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # Close the session
        session.close()

if __name__ == "__main__":
    main()
