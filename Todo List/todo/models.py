from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Todo(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, nullable=False)
    is_complete = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship("User", back_populates="tasks")  


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    tasks = relationship("Todo", back_populates="creator") 
