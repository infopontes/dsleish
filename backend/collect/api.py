import uuid
from ninja import Router
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from .models import Collect

from datetime import date

# Creating a router to organize this app's routes
router = Router()

class GsearchSchema(BaseModel):
    id_search_group: Optional[uuid.UUID]
    name: Optional[str]

    class Config:
        orm_mode = True


class AnimalSchema(BaseModel):
    id_animal: Optional[uuid.UUID]
    name: Optional[str]
    
    class Config:
        orm_mode = True


class CollectSchema(BaseModel):
    id: Optional[uuid.UUID] = None
    dt_collection: Optional[date] = None
    id_search_group: Optional[GsearchSchema]
    id_animal: Optional[AnimalSchema]
    latitude: Optional[str]
    longitude: Optional[str]
    score: Optional[int]
    serum: Optional[bool]
    plasma: Optional[bool]
    marrow_aspirate: Optional[bool]
    lymph_node_aspirate: Optional[bool]
    lymph_node_aspirate_dna: Optional[str]
    strains: Optional[str]
    dna_strains: Optional[str]
    age: Optional[str]
    parasite_slide: Optional[str]
    location_slide: Optional[str]
    parasite_culture: Optional[str]
    location_culture: Optional[str]
    sorology_rifi: Optional[str]
    dilution: Optional[int]
    sorology_dpp: Optional[str]
    fiocruz_elisa: Optional[str]
    biomanguinhos_elisa: Optional[str]
    general_state: Optional[int]
    ecto_paras: Optional[int]
    nutritional_status: Optional[int]
    observation: Optional[str]
    coat: Optional[int]
    nails: Optional[int]
    mucous_coloring: Optional[str]
    muzzle_injury: Optional[int]
    observation_muzzle_injury: Optional[str]
    lymph_node: Optional[int]
    observation_lymph_node: Optional[str]
    blepharitis: Optional[int]
    conjunctivitis: Optional[int]
    observation_conjunctivitis: Optional[str]
    alopecia: Optional[int]
    observation_alopecia: Optional[str]
    bleeding: Optional[int]
    skin_injury: Optional[int]
    observation_skin_injury: Optional[str]
    muzzle_depigmentation: Optional[int]
    
    class Config:
        orm_mode = True
        
    @field_validator('serum', 'plasma', 'marrow_aspirate', 'lymph_node_aspirate', mode='before')
    def validate_boolean(cls, value):
        if isinstance(value, str):
            if value.upper() == 'SIM':
                return True
            elif value.upper() == 'NÃO':
                return False
        return value


@router.get("/list_collect/", response=List[CollectSchema])
def list_collect(request):
    collects = Collect.objects.select_related('id_search_group', 'id_animal').all()

    collect_list = [
        {
            'id': collect.id,
            'dt_collection': collect.dt_collection,
            'id_search_group': {'id_search_group': collect.id_search_group.id, 'name': collect.id_search_group.name} if collect.id_search_group else None,
            'id_animal': {'id_animal': collect.id_animal.id, 'name': collect.id_animal.name} if collect.id_animal else None,
            'latitude': collect.latitude,
            'longitude': collect.longitude,
            'score': collect.score,
            'serum': collect.serum,
            'plasma': collect.plasma,
            'marrow_aspirate': collect.marrow_aspirate,
            'lymph_node_aspirate': collect.lymph_node_aspirate,
            'lymph_node_aspirate_dna': collect.lymph_node_aspirate_dna,
            'strains': collect.strains,
            'dna_strains': collect.dna_strains,
            'age': collect.age,
            'parasite_slide': collect.parasite_slide,
            'location_slide': collect.location_slide,
            'parasite_culture': collect.parasite_culture,
            'location_culture': collect.location_culture,
            'sorology_rifi': collect.sorology_rifi,
            'dilution': collect.dilution,
            'sorology_dpp': collect.sorology_dpp,
            'fiocruz_elisa': collect.fiocruz_elisa,
            'biomanguinhos_elisa': collect.biomanguinhos_elisa,
            'general_state': collect.general_state,
            'ecto_paras': collect.ecto_paras,
            'nutritional_status': collect.nutritional_status,
            'observation': collect.observation,
            'coat': collect.coat,
            'nails': collect.nails,
            'mucous_coloring': collect.mucous_coloring,
            'muzzle_injury': collect.muzzle_injury,
            'observation_muzzle_injury': collect.observation_muzzle_injury,
            'lymph_node': collect.lymph_node,
            'observation_lymph_node': collect.observation_lymph_node,
            'blepharitis': collect.blepharitis,
            'conjunctivitis': collect.conjunctivitis,
            'observation_conjunctivitis': collect.observation_conjuntivitis,
            'alopecia': collect.alopecia,
            'observation_alopecia': collect.observation_alopecia,
            'bleeding': collect.bleeding,
            'skin_injury': collect.skin_injury,
            'observation_skin_injury': collect.observation_skin_injury,
            'muzzle_depigmentation': collect.muzzle_depigmentation,
        }
        for collect in collects
    ]

    return collect_list