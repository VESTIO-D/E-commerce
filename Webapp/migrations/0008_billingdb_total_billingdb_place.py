# Generated by Django 5.0.4 on 2024-06-10 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0007_rename_mobile_billingdb_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingdb',
            name='Total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='billingdb',
            name='place',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
