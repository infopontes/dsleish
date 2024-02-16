from django.urls import path

from backend.breed import views as v

app_name = 'race'

urlpatterns = [
    # path('', v.RaceListView.as_view(), name='race_list'),
    # path('create/', v.RaceCreateView.as_view(), name='race_create'),
    # path('<int:pk>/', v.RaceDetailView.as_view(), name='race_detail'),
    # path('<int:pk>/update/', v.ExpenseUpdateView.as_view(), name='race_update'),
    # path('<int:pk>/delete/', v.race_delete, name='race_delete'),
]