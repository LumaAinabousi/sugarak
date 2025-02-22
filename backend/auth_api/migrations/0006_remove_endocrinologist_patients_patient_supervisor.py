# Generated by Django 5.1.3 on 2024-12-27 22:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0005_endocrinologist_patients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endocrinologist',
            name='patients',
        ),
        migrations.AddField(
            model_name='patient',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patients', to='auth_api.endocrinologist'),
        ),
    ]
