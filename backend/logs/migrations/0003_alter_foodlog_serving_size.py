# Generated by Django 5.1.3 on 2025-01-04 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_alter_exerciselog_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodlog',
            name='serving_size',
            field=models.FloatField(max_length=50),
        ),
    ]
