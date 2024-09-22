import uuid
from ninja import Router
from pydantic import BaseModel
from typing import List, Optional
from .models import Animal

# Creating a router to organize this app's routes
router = Router()

class BreedSchema(BaseModel):
    name: Optional[str]

    class Config:
        orm_mode = True


class CoatSchema(BaseModel):
    name: Optional[str]
    
    class Config:
        orm_mode = True
        

# Creating a router Animal
class AnimalSchema(BaseModel):
    id: Optional[uuid.UUID] = uuid.uuid4()
    id_db_original: Optional[str]
    name: Optional[str]
    name_chip: Optional[str]
    sex: Optional[str]
    breed: Optional[BreedSchema]
    age: Optional[str]
    coat: Optional[CoatSchema]
    owner: Optional[str]
    phone_number: Optional[str]
    

    class Config:
        orm_mode = True


@router.get("/list_animal/", response=List[AnimalSchema])
def list_animal(request):
    animals = Animal.objects.select_related('breed', 'coat').all()

    animals_list = [
        {
            'id': animal.id,
            'id_db_original': animal.id_db_original,
            'name': animal.name,
            'name_chip': animal.name_chip,
            'sex': animal.sex,
            'breed': {'name': animal.breed.name} if animal.breed else None,
            'age': animal.age,
            'coat': {'name': animal.coat.name} if animal.coat else None,
            'owner': animal.owner,
            'phone_number': animal.phone_number,
        }
        for animal in animals
    ]

    return animals_list

# End Animal