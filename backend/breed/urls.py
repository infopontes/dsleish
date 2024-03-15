from django.urls import path

from backend.breed import views as v
from backend.breed import views_htmx as vx

app_name = 'breed'

urlpatterns = [
    path('', v.BreedListView.as_view(), name='breed_list'),
    path('create/', v.BreedCreateView.as_view(), name='breed_create'),
    path('<uuid:pk>/', v.BreedDetailView.as_view(), name='breed_detail'),
    path('<uuid:pk>/update/', v.BreedUpdateView.as_view(), name='breed_update'),
    path('<uuid:pk>/delete/', v.BreedDeleteView.as_view(), name='breed_delete'),
]

htmx_urlpatterns =[
    path('check_breed/', vx.check_breed, name="check_breed"),
]

urlpatterns += htmx_urlpatterns