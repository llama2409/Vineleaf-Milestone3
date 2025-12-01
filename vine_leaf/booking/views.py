from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def booking_page(request):
    return render(request, 'booking.html')