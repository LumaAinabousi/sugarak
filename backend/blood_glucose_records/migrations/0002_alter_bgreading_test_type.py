# Generated by Django 5.1.3 on 2025-01-02 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_glucose_records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bgreading',
            name='test_type',
            field=models.CharField(choices=[('fasting', 'Fasting'), ('random', 'Random')], max_length=50),
        ),
    ]
