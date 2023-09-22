import sys
import os

# Add the project directory to sys.path
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_dir)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_dir.models import Animal, MilkProductionRecord

# Create a database connection
engine = create_engine('mysql+mysqlconnector://farmanager:manage123@localhost/farmgt')
Session = sessionmaker(bind=engine)
session = Session()

# Retrieve animals and their milk production records
animals = session.query(Animal).all()

# Print the list of animals and their milk production records
for animal in animals:
    print(f"Animal: {animal.name} ({animal.breed})")
    print("Milk Production Records:")
    for record in animal.milk_production_records:
        print(f"Date: {record.date_of_production}, Amount: {record.amount_produced}, Notes: {record.notes}")
    print("=" * 40)

# Close the session
session.close()
