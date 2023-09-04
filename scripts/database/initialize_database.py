# Import necessary modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Define database connection URL
DB_URL = 'mysql+mysqlconnector://farmanager:manage123@localhost/farmgt'

# Create a database engine
engine = create_engine(DB_URL)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create database tables based on SQLAlchemy models
Base.metadata.create_all(engine)

# Close the session
session.close()

print("Database tables have been created.")

