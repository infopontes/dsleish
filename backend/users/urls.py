from django.urls import path

from backend.users import views as v


app_name = 'users'

urlpatterns = [
    path('<int:pk>/update/', v.UserUpdateView.as_view(), name='user_update'),
    path('password/', v.PasswordsChangeView.as_view(template_name='users/change-password.html'), name='password'),
    path('password_success', v.password_success, name = 'password_success'),
]