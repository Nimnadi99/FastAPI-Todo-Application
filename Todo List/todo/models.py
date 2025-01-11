from .database import Base
from sqlalchemy import Column, Integer, String, Boolean


class Todo(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key= True, index= True)
    task = Column(String)
    is_complete = Column(Boolean)