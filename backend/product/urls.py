from django.urls import path, include

from product import views

urlpatterns = [
    path("productsList/", views.ProductsList.as_view()),
]
