from pydantic import BaseModel
from typing import Optional, List

class Todo(BaseModel):
    task: str
    is_complete : Optional[bool]
    
    class Config():
        orm_mode = True
    

class User(BaseModel):
    username : str
    email : str
    password : str
    
    class Config():
        orm_mode = True
        
class ShowUser(BaseModel):
    username : str
    email : str
    
    class Config():
        orm_mode = True
        
class showTask(Todo):
    pass
    creator: ShowUser
    class Config:
        orm_mode = True
        
class Login(BaseModel):
    username: str
    password: str
    
    class Config:
        orm_mode = True
        
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None