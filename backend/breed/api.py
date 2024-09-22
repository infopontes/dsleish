import uuid
from ninja import Router
from pydantic import BaseModel
from typing import List, Optional
from .models import Breed

# Creating a router to organize this app's routes
router = Router()

class SpecieSchema(BaseModel):
    name: Optional[str]

    class Config:
        orm_mode = True


# Creating class Breed
class BreedSchema(BaseModel):
    id: Optional[uuid.UUID] = uuid.uuid4()
    name: Optional[str]
    description: Optional[str]
    specie: Optional[SpecieSchema]
    
    class Config:
        orm_mode = True


@router.get("/list_breed/", response=List[BreedSchema])
def list_breed(request):
    breeds = Breed.objects.select_related('specie').all()

    breeds_list = [
        {
            'name': breed.name,
            'description': breed.description,
            'specie': {'name': breed.specie.name} if breed.specie else None,
        }
        for breed in breeds
    ]

    return breeds_list