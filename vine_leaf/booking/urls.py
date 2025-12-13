from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('booking/', views.booking_page, name='booking'),
    path('menus/', views.menus_page, name='menus'),
    path('contact/', views.contact_page, name='contact'),
    path('booking/success/<int:pk>/', views.booking_success, name='booking_success'),
    path('booking/edit/<int:pk>/', views.edit_booking, name='edit_booking'),
    path('booking/delete/<int:pk>/', views.delete_booking, name='delete_booking'),
]