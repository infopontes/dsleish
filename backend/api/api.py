from ninja import NinjaAPI
from backend.animal.api import router as animal_router
from backend.breed.api import router as breed_router
from backend.coat.api import router as coat_router
from backend.collect.api import router as collect_router
from backend.gsearch.api import router as gsearch_router

api = NinjaAPI()

# Incluindo as rotas dos outros apps
api.add_router("/animal/", animal_router)
api.add_router("/breed/", breed_router)
api.add_router("/coat/", coat_router)
api.add_router("/collect/", collect_router)
api.add_router("/gsearch/", gsearch_router)