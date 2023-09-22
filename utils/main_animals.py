import sys
import os

# Add the project directory to sys.path
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_dir)

"""project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)"""

from sqlalchemy.orm import sessionmaker
from database_dir.database import engine, Session
from database_dir.models import Animal, MilkProductionRecord

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

def main():
    # Create a new animal
    new_animal = Animal(name='sandy', breed='guernsey', birth_date='2021-02-13', gender='Female')
    session.add(new_animal)
    session.commit()

    # Create a new milk production record for the animal
    new_milk_production = MilkProductionRecord(cow_id=new_animal.id, date_of_production='2023-06-18', amount_produced='16')
    session.add(new_milk_production)
    session.commit()

    print("Animal and milk production record added successfully.")

if __name__ == "__main__":
    main()
