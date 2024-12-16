from django.urls import path, include
from . import views

# /api/products/
urlpatterns = [
    path("<int:pk>/", views.ProductDetailAPIView.as_view()),
    path("", views.ProductListCreateAPIView.as_view())
]