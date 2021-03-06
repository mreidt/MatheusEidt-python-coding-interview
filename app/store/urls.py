from django.urls import path

from .views import ListProducts

app_name = "store"

urlpatterns = [
    path("products/", ListProducts.as_view()),
    path("products/<int:pk>", ListProducts.as_view()),
]
