# Generated by Django 5.0.6 on 2024-07-01 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='description',
            new_name='issue_description',
        ),
    ]