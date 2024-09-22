import uuid
from ninja import Router
from pydantic import BaseModel
from typing import List, Optional
from .models import Coat

# Creating a router to organize this app's routes
router = Router()

# Creating class Coat
class CoatSchema(BaseModel):
    id: Optional[uuid.UUID] = uuid.uuid4()
    name: Optional[str]
    description: Optional[str]
    
    class Config:
        orm_mode = True


@router.get("/list_coat/", response=List[CoatSchema])
def list_coat(request):
    coats = Coat.objects.all()

    coats_list = [
        {
            'id': coat.id,
            'name': coat.name,
            'description': coat.description,
        }
        for coat in coats
    ]

    return coats_list