# Generated by Django 4.1.6 on 2023-02-22 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_location_skill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['created']},
        ),
    ]