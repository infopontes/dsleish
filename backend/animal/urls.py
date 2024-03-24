from django.urls import path

from backend.animal import views as v
from backend.animal import views_htmx as vx

app_name = 'animal'

urlpatterns = [
    path('', v.AnimalListView.as_view(), name='animal_list'),
    path('create/', v.AnimalCreateView.as_view(), name='animal_create'),
    path('<uuid:pk>/', v.AnimalDetailView.as_view(), name='animal_detail'),
    path('<uuid:pk>/update/', v.AnimalUpdateView.as_view(), name='animal_update'),
    path('<uuid:pk>/delete/', v.AnimalDeleteView.as_view(), name='animal_delete'),
]

htmx_urlpatterns =[
    path('check_animal/', vx.check_animal, name="check_animal"),
]

urlpatterns += htmx_urlpatterns