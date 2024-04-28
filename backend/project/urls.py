from django.urls import path

from backend.project import views as v
# from backend.animal import views_htmx as vx

app_name = 'project'

urlpatterns = [
    path('', v.ProjectListView.as_view(), name='project_list'),
    path('create/', v.ProjectCreateView.as_view(), name='project_create'),
    path('<uuid:pk>/', v.ProjectDetailView.as_view(), name='project_detail'),
    path('<uuid:pk>/update/', v.ProjectUpdateView.as_view(), name='project_update'),
    path('<uuid:pk>/delete/', v.ProjectDeleteView.as_view(), name='project_delete'),
]

# htmx_urlpatterns =[
#     path('check_animal/', vx.check_animal, name="check_animal"),
# ]

# urlpatterns += htmx_urlpatterns