# Generated by Django 5.1.4 on 2025-01-20 05:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Launch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_name', models.CharField(max_length=200)),
                ('launch_date', models.DateTimeField()),
                ('launch_site', models.CharField(max_length=200)),
                ('mission_patch', models.URLField(blank=True, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('webcast_link', models.URLField(blank=True, null=True)),
                ('success', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rocket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rocket_id', models.CharField(max_length=100, unique=True)),
                ('rocket_name', models.CharField(max_length=100)),
                ('rocket_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payload_id', models.CharField(max_length=100, unique=True)),
                ('payload_type', models.CharField(max_length=100)),
                ('payload_mass_kg', models.FloatField(blank=True, null=True)),
                ('orbit', models.CharField(max_length=100)),
                ('launch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payloads', to='spacex_tracker.launch')),
            ],
        ),
        migrations.AddField(
            model_name='launch',
            name='rocket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='launches', to='spacex_tracker.rocket'),
        ),
    ]
