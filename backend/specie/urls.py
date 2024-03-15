from django.urls import path

from backend.specie import views as v

from backend.specie import views_htmx as vx

app_name = 'specie'

urlpatterns = [
    path('', v.SpecieListView.as_view(), name='specie_list'),
    path('create/', v.SpecieCreateView.as_view(), name='specie_create'),
    path('<uuid:pk>/', v.SpecieDetailView.as_view(), name='specie_detail'),
    path('<uuid:pk>/update/', v.SpecieUpdateView.as_view(), name='specie_update'),
    path('<uuid:pk>/delete/', v.SpecieDeleteView.as_view(), name='specie_delete'),
]

htmx_urlpatterns =[
    path('check_specie/', vx.check_specie, name="check_specie"),
]

urlpatterns += htmx_urlpatterns