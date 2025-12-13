from django import forms
from django.utils import timezone
from datetime import time, datetime, timedelta
from .models import Booking


def generate_time_choices():
    times = []
    start = datetime.strptime("17:00", "%H:%M")
    end = datetime.strptime("22:00", "%H:%M")

    while start <= end:
        times.append(
            (start.strftime("%H:%M"), start.strftime("%H:%M"))
        )
        start += timedelta(minutes=30)

    return times


class BookingForm(forms.ModelForm):

    time = forms.ChoiceField(choices=generate_time_choices())

    class Meta:
        model = Booking
        fields = ['name', 'email', 'date', 'time', 'guests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time_str = cleaned_data.get('time')

        if date and time_str:

            hour, minute = map(int, time_str.split(':'))
            chosen_time = time(hour, minute)

            cleaned_data['time'] = chosen_time

            # Prevent double-booking
            existing = Booking.objects.filter(
                date=date,
                time=chosen_time
            )

            if self.instance.pk:
                existing = existing.exclude(pk=self.instance.pk)

            if existing.exists():
                raise forms.ValidationError(
                    "This time slot is already booked. Please choose another time."
                )

            # Prevent bookings < 2 hrs away
            booking_datetime = datetime.combine(date, chosen_time)
            booking_datetime = timezone.make_aware(booking_datetime)
            now = timezone.now()

            if booking_datetime < now + timedelta(hours=2):
                raise forms.ValidationError(
                    "Bookings must be made at least 2 hours in advance."
                )

        return cleaned_data
