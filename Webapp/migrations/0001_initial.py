# Generated by Django 5.0.4 on 2024-05-11 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='servicedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('subject', models.CharField(blank=True, max_length=50, null=True)),
                ('message', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]