# Generated by Django 5.0.4 on 2024-05-31 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0002_regdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(blank=True, max_length=50, null=True)),
                ('pname', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]