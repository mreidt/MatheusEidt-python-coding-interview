from django.urls import path
from .views import ListUsers

app_name = 'users'

urlpatterns = [
    path('users', ListUsers.as_view()),
]
