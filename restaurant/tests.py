from datetime import timedelta
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIClient
from .models import Booking, MenuItem

class RestaurantAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username="tester", password="StrongTestPass123!")
        self.manager = get_user_model().objects.create_user(username="manager", password="StrongTestPass123!", is_staff=True)
        MenuItem.objects.create(title="Greek Salad", price="12.50", inventory=20)
    def test_menu_list_is_public(self):
        response = self.client.get("/api/menu/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any(x["title"] == "Greek Salad" for x in response.data["results"]))
    def test_anonymous_user_cannot_create_menu_item(self):
        response = self.client.post("/api/menu/", {"title": "Pasta", "price": "15.00", "inventory": 5})
        self.assertEqual(response.status_code, 401)
    def test_manager_can_create_menu_item(self):
        self.client.force_authenticate(user=self.manager)
        response = self.client.post("/api/menu/", {"title": "Pasta", "price": "15.00", "inventory": 5})
        self.assertEqual(response.status_code, 201)
    def test_booking_requires_authentication(self):
        response = self.client.get("/api/bookings/")
        self.assertEqual(response.status_code, 401)
    def test_authenticated_user_can_create_booking(self):
        self.client.force_authenticate(user=self.user)
        future = (timezone.now() + timedelta(days=2)).isoformat()
        response = self.client.post("/api/bookings/", {"name": "Sam", "no_of_guests": 2, "booking_date": future}, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Booking.objects.count(), 1)
    def test_users_only_see_their_own_bookings(self):
        Booking.objects.create(name="Other", no_of_guests=2, booking_date=timezone.now() + timedelta(days=3), user=self.manager)
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/api/bookings/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 0)
    def test_registration_endpoint(self):
        response = self.client.post("/api/auth/users/", {"username": "newuser", "password": "AnotherStrongPass123!", "re_password": "AnotherStrongPass123!"}, format="json")
        self.assertEqual(response.status_code, 201)
