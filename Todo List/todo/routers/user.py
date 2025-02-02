from fastapi import APIRouter, Depends, status, HTTPException
from .. import database, schemas, models
from sqlalchemy.orm import Session
from ..hashing import Hash
from typing import List


router = APIRouter(
    prefix= "/user",
    tags= ["User"]
)

get_db = database.get_db

# Create User
@router.post('/')
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    new_user = models.User(username = request.username, email = request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# Show Users
@router.get('/', response_model= List[schemas.ShowUser])
def show_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users available!")
    return users
    
# Show User
@router.get('/{id}', response_model= schemas.ShowUser)
def show_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'User with the id {id} is not exist')
    return user
