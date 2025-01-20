from django.contrib import admin
from .models import Launch, Rocket, Payload

@admin.register(Launch)
class LaunchAdmin(admin.ModelAdmin):
    list_display = ('mission_name', 'launch_date', 'rocket', 'success')
    list_filter = ('success', 'rocket')

@admin.register(Rocket)
class RocketAdmin(admin.ModelAdmin):
    list_display = ('rocket_name', 'rocket_type')

@admin.register(Payload)
class PayloadAdmin(admin.ModelAdmin):
    list_display = ('payload_id', 'payload_type', 'payload_mass_kg', 'orbit')
