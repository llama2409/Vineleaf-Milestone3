from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('booking/', views.booking_page, name='booking'),
    path('menus/', views.menus_page, name='menus'),
]