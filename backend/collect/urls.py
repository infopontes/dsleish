from django.urls import path

from backend.collect import views as v
#from backend.collect import views_htmx as vx

app_name = 'collect'

urlpatterns = [
    path('', v.CollectListView.as_view(), name='collect_list'),
    path('create/', v.CollectCreateView.as_view(), name='collect_create'),
    path('<uuid:pk>/', v.CollectDetailView.as_view(), name='collect_detail'),
    path('<uuid:pk>/update/', v.CollectUpdateView.as_view(), name='collect_update'),
    path('<uuid:pk>/delete/', v.CollectDeleteView.as_view(), name='collect_delete'),
]

# htmx_urlpatterns =[
#     path('check_animal/', vx.check_animal, name="check_animal"),
# ]

# urlpatterns += htmx_urlpatterns