# Generated by Django 3.2.18 on 2023-04-30 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_s_liked_event_is_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='eventhandler/frontend/public/'),
        ),
    ]
