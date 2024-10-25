from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the base class for the ORM models
Base = declarative_base()

class DatabaseManager:
    def __init__(self, db_name):
        """Initialize the SQLite database and create tables"""
        self.engine = create_engine(f'sqlite:///{db_name}')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
