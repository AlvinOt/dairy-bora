# database/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the database URL
DATABASE_URL = "mysql+mysqlconnector://farmanager:manage123@localhost/farmgt"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session class to manage interactions with the database
Session = sessionmaker(bind=engine)
