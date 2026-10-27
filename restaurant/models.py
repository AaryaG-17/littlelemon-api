from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    inventory = models.PositiveSmallIntegerField(default=0)
    class Meta:
        ordering = ["title"]
    def __str__(self):
        return self.title

class Booking(models.Model):
    name = models.CharField(max_length=100)
    no_of_guests = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    booking_date = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="restaurant_bookings")
    class Meta:
        ordering = ["booking_date"]
    def __str__(self):
        return f"{self.name} ({self.no_of_guests}) at {self.booking_date}"
