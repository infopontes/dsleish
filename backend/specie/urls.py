from django.urls import path

from backend.specie import views as v

app_name = 'specie'

urlpatterns = [
    path('', v.SpecieListView.as_view(), name='specie_list'),
    path('create/', v.SpecieCreateView.as_view(), name='specie_create'),
    path('<uuid:pk>/', v.SpecieDetailView.as_view(), name='specie_detail'),
    path('<uuid:pk>/update/', v.SpecieUpdateView.as_view(), name='specie_update'),
    path('<uuid:pk>/delete/', v.specie_delete, name='specie_delete'),
]