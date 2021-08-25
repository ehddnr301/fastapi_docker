import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv(verbose=True)

NAME = os.getenv('NAME')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
DB = os.getenv('DB')

print(NAME, PASSWORD, HOST, DB)
SQLALCHEMY_DATABASE_URL = f'postgresql://{NAME}:{PASSWORD}@{HOST}/{DB}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

