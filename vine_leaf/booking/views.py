from django.shortcuts import render, redirect
from .forms import BookingForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def booking_page(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})


def booking_success(request):
    return render(request, 'booking_success.html')


def menus_page(request):
    return render(request, 'menus.html')


def contact_page(request):
    return render(request, 'contact.html')