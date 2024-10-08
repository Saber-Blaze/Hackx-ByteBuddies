# Generated by Django 5.1 on 2024-09-05 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorRecord',
            fields=[
                ('uid', models.CharField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('specialization', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='PatientRecord',
            fields=[
                ('uid', models.CharField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('emergency_contact_number', models.CharField(max_length=15)),
                ('chronic_conditions', models.JSONField()),
                ('blood_type', models.CharField(max_length=3)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('blood_pressure', models.CharField(max_length=10)),
                ('body_temperature', models.FloatField()),
                ('heart_rate', models.IntegerField()),
                ('respiratory_rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication_name', models.CharField(max_length=255)),
                ('dosage', models.CharField(max_length=255)),
                ('frequency', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medications', to='EHR.patientrecord')),
            ],
        ),
    ]
