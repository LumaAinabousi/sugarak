# Generated by Django 5.1.3 on 2025-01-05 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0003_alter_foodlog_serving_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodlog',
            name='calories',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
