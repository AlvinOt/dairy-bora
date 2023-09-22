from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Animal(Base):
    __tablename__ = 'animals'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    breed = Column(String(100))
    birth_date = Column(Date)
    gender = Column(String(10))
    health_information = Column(String(255))  # Health information of the animal
    reproductive_status = Column(String(255))  # Reproductive status of the animal

    milk_production_records = relationship('MilkProductionRecord', back_populates='animal')
    animal_health_records = relationship('AnimalHealthRecord', back_populates='animal')
    reproductive_records = relationship('ReproductiveRecord', back_populates='animal')
    feed_and_nutrition_records = relationship('FeedNutritionRecord', back_populates='animal')

class MilkProductionRecord(Base):
    __tablename__ = 'milk_production_records'

    id = Column(Integer, primary_key=True)
    cow_id = Column(Integer, ForeignKey('animals.id'))
    date_of_production = Column(Date)
    amount_produced = Column(Float)
    notes = Column(String(255))

    animal = relationship('Animal', back_populates='milk_production_records')

class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True)
    item_name = Column(String(50))
    quantity = Column(Integer)
    unit_of_measurement = Column(String(20))
    expiry_date = Column(Date)
    purchase_date = Column(Date)
    supplier_information = Column(String(128))
    usage_tracking = Column(String(255))

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True)
    password_hashed = Column(String(64))
    role = Column(String(20))
    contact_information = Column(String(50))

    user_reports = relationship('Report', back_populates='user')

class AnimalHealthRecord(Base):
    __tablename__ = 'animal_health_records'

    id = Column(Integer, primary_key=True)
    cow_id = Column(Integer, ForeignKey('animals.id'))
    date_of_record = Column(Date)
    health_issue = Column(String(50))
    medication_given = Column(String(50))
    notes = Column(String(255))

    animal = relationship('Animal', back_populates='animal_health_records')

class ReproductiveRecord(Base):
    __tablename__ = 'reproductive_records'

    id = Column(Integer, primary_key=True)
    cow_id = Column(Integer, ForeignKey('animals.id'))
    date_of_record = Column(Date)
    reproductive_event = Column(String(100))
    outcome = Column(String(50))

    animal = relationship('Animal', back_populates='reproductive_records')

class FinancialRecord(Base):
    __tablename__ = 'financial_records'

    id = Column(Integer, primary_key=True)
    transaction_date = Column(Date)
    transaction_type = Column(String(50))
    amount = Column(Float)
    description = Column(String(100))
    payment_method = Column(String(50))

class Report(Base):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True)
    report_type = Column(String(50))
    date_generated = Column(Date)
    content = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='user_reports')

class FeedNutritionRecord(Base):
    __tablename__ = 'feed_nutrition_records'

    id = Column(Integer, primary_key=True)
    cow_id = Column(Integer, ForeignKey('animals.id'))
    date_of_record = Column(Date)
    feed_type = Column(String(20))
    quantity_given = Column(Float)
    nutritional_information = Column(String(100))
    feeding_schedule = Column(String(100))

    animal = relationship('Animal', back_populates='feed_and_nutrition_records')

# Add other models here if need be

# Engine creation
engine = create_engine('mysql+mysqlconnector://farmanager:manage123@localhost/farmgt')
Base.metadata.create_all(engine)
