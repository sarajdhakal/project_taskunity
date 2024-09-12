# Generated by Django 5.0.6 on 2024-09-12 03:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_remove_room_check1_remove_room_check2_room_user1_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='team_members',
            field=models.ManyToManyField(blank=True, related_name='team_members', to=settings.AUTH_USER_MODEL),
        ),
    ]