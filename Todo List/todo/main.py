from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session



app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# create task
@app.post('/todo', status_code= status.HTTP_201_CREATED)
def create(request: schemas.Todo, db: Session = Depends(get_db)):
    new_task = models.Todo(task = request.task, is_complete = request.is_complete)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

# Get Tasks
@app.get('/todo')
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Todo).all()
    if not tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No tasks available!")
    return tasks

# Get Task
@app.get("/todo/{id}")
def get_task(id, db: Session = Depends(get_db)):
    task = db.query(models.Todo).filter(models.Todo.id == id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Task with id {id} not found !!')    

    return task



# Delete All Tasks
@app.delete("/todo")
def delete_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Todo).all()
    if not tasks:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='No Tasks Found')
    db.query(models.Todo).delete(synchronize_session=False)
    db.commit()
    return {"message" : "All the Tasks deleted...."}



# Delete Task
@app.delete("/todo/{id}")
def delete_task(id, db: Session = Depends(get_db)):
    task = db.query(models.Todo).filter(models.Todo.id == id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Task with id {id} not found !!')
    db.delete(task)  
    db.commit()
    return {"message": f"Task has been deleted."}



# Update Task
@app.put("/todo/{id}")
def update_task(id: int, request: schemas.Todo , db: Session = Depends(get_db)):
    task = db.query(models.Todo).filter(models.Todo.id == id)
    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Task with id {id} not found!!')
    task.update(request.dict())  
    db.commit()  
    return {'detail': 'Updated successfully!'}

    
    
