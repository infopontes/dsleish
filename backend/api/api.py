from ninja import NinjaAPI
from backend.animal.api import router as animal_router
from backend.breed.api import router as breed_router

api = NinjaAPI()

# Incluindo as rotas dos outros apps
api.add_router("/animal/", animal_router)
api.add_router("/breed/", breed_router)