from django.utils import timezone
from rest_framework import serializers
from .models import Booking, MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["id", "title", "price", "inventory"]

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Booking
        fields = ["id", "name", "no_of_guests", "booking_date", "user"]
    def validate_booking_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Booking date must be in the future.")
        return value
