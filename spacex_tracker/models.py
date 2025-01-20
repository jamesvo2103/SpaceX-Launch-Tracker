from django.db import models

# Create your models here.
class Launch(models.Model):
    mission_name = models.CharField(max_length=200)
    launch_date = models.DateTimeField()
    rocket = models.ForeignKey('Rocket', on_delete=models.CASCADE, related_name='launches')
    launch_site = models.CharField(max_length=200)
    mission_patch = models.URLField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    webcast_link = models.URLField(null=True, blank=True)
    success = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.mission_name

class Rocket(models.Model):
    rocket_id = models.CharField(max_length=100, unique=True)
    rocket_name = models.CharField(max_length=100)
    rocket_type = models.CharField(max_length=100)

    def __str__(self):
        return self.rocket_name

class Payload(models.Model):
    payload_id = models.CharField(max_length=100, unique=True)
    payload_type = models.CharField(max_length=100)
    payload_mass_kg = models.FloatField(null=True, blank=True)
    orbit = models.CharField(max_length=100)
    launch = models.ForeignKey(Launch, on_delete=models.CASCADE, related_name='payloads')

    def __str__(self):
        return self.payload_id
