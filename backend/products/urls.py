from django.urls import path, include
from . import views

# /api/products/
urlpatterns = [
    path("<int:pk>/", views.ProductMixinView.as_view()),
    path("<int:pk>/update/", views.ProductUpdateAPIView.as_view()),
    path("<int:pk>/delete/", views.ProductDeleteAPIView.as_view()),
    path("", views.ProductListCreateAPIView.as_view())
]