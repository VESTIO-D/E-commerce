# Generated by Django 5.0.4 on 2024-06-08 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0006_billingdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingdb',
            old_name='mobile',
            new_name='phone',
        ),
    ]
