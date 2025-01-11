from pydantic import BaseModel
from typing import Optional

class Todo(BaseModel):
    task: str
    is_complete : Optional[bool]