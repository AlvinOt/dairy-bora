import sys
import os

# Add the project root directory to the Python path
"""project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)"""

from sqlalchemy.orm import sessionmaker
from database.database import engine, Session
from database.models import Animal, MilkProductionRecord

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

def main():
    # Create a new animal
    new_animal = Animal(name='mercy', breed='guernsey', birth_date='2021-02-13', gender='Female')
    session.add(new_animal)
    session.commit()

    # Create a new milk production record for the animal
    new_milk_production = MilkProductionRecord(cow_id=new_animal.id, date_of_production='2023-06-13', amount_produced=12.5)
    session.add(new_milk_production)
    session.commit()

    print("Animal and milk production record added successfully.")

if __name__ == "__main__":
    main()
