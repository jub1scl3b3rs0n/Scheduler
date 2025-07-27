from django.db import models
from django.contrib.auth.models import User

class ServiceProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    available_days = models.JSONField(default=dict)  # {"monday": ["09:00", "10:00"]}

    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE, related_name="appointments")
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=[
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled")
    ], default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['provider', 'date', 'time']

    def __str__(self):
        return f"{self.date} {self.time} - {self.provider.user.username}"
