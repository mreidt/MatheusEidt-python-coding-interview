from django.urls import path
from .views import Welcome

app_name = 'main'

urlpatterns = [
    path('', Welcome.as_view()),
]