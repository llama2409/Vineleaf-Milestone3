from django import forms
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date', 'time', 'guests']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if date and time:
            existing = Booking.objects.filter(date=date, time=time).exists()
            if existing:
                raise forms.ValidationError("This time slot is already booked. Please choose another time.")
            
            booking_datetime = datetime.combine(date, time)
            booking_datetime = timezone.make_aware(booking_datetime)

            now = timezone.now()
            if booking_datetime < now + timedelta(hours=2):
                raise forms.ValidationError("Bookings must be made at least 2 hoursin advance.")

        return cleaned_data