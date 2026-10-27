import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(name="MenuItem", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("title", models.CharField(max_length=100)),
            ("price", models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0)])),
            ("inventory", models.PositiveSmallIntegerField(default=0)),
        ], options={"ordering": ["title"]}),
        migrations.CreateModel(name="Booking", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(max_length=100)),
            ("no_of_guests", models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ("booking_date", models.DateTimeField()),
            ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="restaurant_bookings", to=settings.AUTH_USER_MODEL)),
        ], options={"ordering": ["booking_date"]}),
    ]
