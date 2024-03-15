from django.urls import path

from backend.coat import views as v
from backend.coat import views_htmx as vx

app_name = 'coat'

urlpatterns = [
    path('', v.CoatListView.as_view(), name='coat_list'),
    path('create/', v.CoatCreateView.as_view(), name='coat_create'),
    path('<uuid:pk>/', v.CoatDetailView.as_view(), name='coat_detail'),
    path('<uuid:pk>/update/', v.CoatUpdateView.as_view(), name='coat_update'),
    path('<uuid:pk>/delete/', v.CoatDeleteView.as_view(), name='coat_delete'),
]

htmx_urlpatterns =[
    path('check_coat/', vx.check_coat, name="check_coat"),
]

urlpatterns += htmx_urlpatterns