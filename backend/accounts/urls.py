from django.urls import path

from backend.accounts import views as v

app_name = 'accounts'

urlpatterns = [
    path('register/', v.SignUp.as_view(), name='register'),
]