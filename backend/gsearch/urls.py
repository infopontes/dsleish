from django.urls import path

from backend.gsearch import views as v
#from backend.animal import views_htmx as vx

app_name = 'gsearch'

urlpatterns = [
    path('', v.GsearchListView.as_view(), name='gsearch_list'),
    path('create/', v.GsearchCreateView.as_view(), name='gsearch_create'),
    path('<uuid:pk>/', v.GsearchDetailView.as_view(), name='gsearch_detail'),
    path('<uuid:pk>/update/', v.GsearchUpdateView.as_view(), name='gsearch_update'),
    path('<uuid:pk>/delete/', v.GsearchDeleteView.as_view(), name='gsearch_delete'),
]

# htmx_urlpatterns =[
#     path('check_animal/', vx.check_animal, name="check_animal"),
# ]

# urlpatterns += htmx_urlpatterns