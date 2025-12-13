from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm
from .models import Booking
# Create your views here.


def home(request):
    return render(request, 'home.html')


def booking_page(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            Booking = form.save()
            return redirect('booking_success', pk=Booking.pk)
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})


def edit_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_success', pk=booking.pk)
    else:
        form = BookingForm(instance=booking)

    return render(request, 'edit_booking.html', {
        'form': form,
        'editing': True,
        'booking': booking,
    })


def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)

    if request.method == 'POST':
        booking.delete()
        return redirect('home')

    return render(request, 'delete_booking.html', {'booking': booking})


def booking_success(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'booking_success.html', {'booking': booking})


def menus_page(request):
    return render(request, 'menus.html')


def contact_page(request):
    return render(request, 'contact.html')