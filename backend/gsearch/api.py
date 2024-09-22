import uuid
from ninja import Router
from pydantic import BaseModel
from typing import List, Optional
from .models import Gsearch

# Creating a router to organize this app's routes
router = Router()

class ProjectSchema(BaseModel):
    id_project: Optional[uuid.UUID]
    name: Optional[str]

    class Config:
        orm_mode = True


class UserSchema(BaseModel):
    id_user: Optional[int]
    first_name: Optional[str]

    class Config:
        orm_mode = True


class GsearchSchema(BaseModel):
    id: Optional[uuid.UUID] = uuid.uuid4()
    id_project: Optional[ProjectSchema]
    id_user: Optional[UserSchema]
    name: Optional[str]
    description: Optional[str]

    class Config:
        orm_mode = True


@router.get("/list_gsearch/", response=List[GsearchSchema])
def list_gsearch(request):
    gsearchs = Gsearch.objects.select_related('project', 'user').all()

    gsearchs_list = [
        GsearchSchema(
            id=gsearch.id,
            id_project=ProjectSchema(
                id_project=gsearch.project.id,
                name=gsearch.project.name
            ) if gsearch.project else None,
            id_user=UserSchema(
                id_user=gsearch.user.id,
                first_name=gsearch.user.first_name
            ) if gsearch.user else None,
            name=gsearch.name,
            description=gsearch.description,
        )
        for gsearch in gsearchs
    ]

    return gsearchs_list

