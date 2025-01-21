from pydantic import BaseModel, Field

class Todo(BaseModel):
    id: int
    title: str = Field(default="Hey", max_length=50)
    created_at: int = Field(..., gt=0) #epoch time
    status: bool = False

