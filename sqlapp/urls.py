from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view),
    path('update/', views.update_view),
]