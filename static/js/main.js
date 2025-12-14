document.addEventListener("DOMContentLoaded", function () {
    const bookingForm = document.querySelector("#booking-form");

    if (bookingForm) {
        bookingForm.addEventListener("submit", function (e) {
            const confirmBooking = confirm(
                "Are you sure you want to submit this booking?"
            );

            if (!confirmBooking) {
                e.preventDefault();
            }
        });
    }
});