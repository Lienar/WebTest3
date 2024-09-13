from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

engine = create_engine("sqlite:///taskmanager.db", echo=True)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

#class User():
#    __tablename__ = "user"

#    username = Column(str)
#    firstname = Column(str)
#    lastname = Column(str)
#    password = Column(str)
#    age = Column(int)

#from app.backend.db import Base
#from app.models.user import User
#from app.models.task import Task
#target_metadata = Base.metadata