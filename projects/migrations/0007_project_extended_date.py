# Generated by Django 5.0.6 on 2024-09-08 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='extended_date',
            field=models.DateField(null=True),
        ),
    ]