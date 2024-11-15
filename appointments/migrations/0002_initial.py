# Generated by Django 5.1.2 on 2024-10-13 00:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointments', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient'),
        ),
    ]
