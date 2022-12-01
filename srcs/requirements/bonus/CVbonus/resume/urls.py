from django.urls import path
from . import views
urlpatterns = [
    path('', views.resume),
    path('CV/', views.resume),
]