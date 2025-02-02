from fastapi import APIRouter, Depends, status, HTTPException
from .. import database, schemas, models, oauth2
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix= "/todo",
    tags= ["Todo"]
)

get_db = database.get_db

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(
    request: schemas.Todo,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user)
):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required"
        )
    
    new_task = models.Todo(
        task=request.task,
        is_complete=request.is_complete,
        user_id=current_user.id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

# Get Tasks
@router.get('/', response_model=List[schemas.showTask])
def get_tasks(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user)
):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required"
        )
    
    tasks = db.query(models.Todo).filter(models.Todo.user_id == current_user.id).all()
    if not tasks:
        return []  
    return tasks

# Get Task
@router.get("/{id}", response_model=schemas.showTask)
def get_task(
    id: int, 
    db: Session = Depends(get_db), 
    current_user: schemas.User = Depends(oauth2.get_current_user)
):
    task = db.query(models.Todo).filter(
        models.Todo.id == id,
        models.Todo.user_id == current_user.id
    ).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Task with id {id} not found !!')    
    return task

# Delete All Tasks
@router.delete("/")
def delete_tasks(
    db: Session = Depends(get_db), 
    current_user: schemas.User = Depends(oauth2.get_current_user)
):
    tasks = db.query(models.Todo).filter(models.Todo.user_id == current_user.id).all()
    if not tasks:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='No Tasks Found')
    db.query(models.Todo).filter(models.Todo.user_id == current_user.id).delete(synchronize_session=False)
    db.commit()
    return {"message" : "All your tasks have been deleted"}

# Delete Task
@router.delete("/{id}")
def delete_task(
    id: int, 
    db: Session = Depends(get_db), 
    current_user: schemas.User = Depends(oauth2.get_current_user)
):
    task = db.query(models.Todo).filter(
        models.Todo.id == id,
        models.Todo.user_id == current_user.id
    ).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Task with id {id} not found !!')
    db.delete(task)  
    db.commit()
    return {"message": f"Task has been deleted"}

# Update Task
@router.put("/{id}")
def update_task(
    id: int, 
    request: schemas.Todo, 
    db: Session = Depends(get_db), 
    current_user: schemas.User = Depends(oauth2.get_current_user)
):
    task = db.query(models.Todo).filter(
        models.Todo.id == id,
        models.Todo.user_id == current_user.id
    )
    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Task with id {id} not found!!')
    task.update(request.dict())  
    db.commit()  
    return {'detail': 'Updated successfully!'}