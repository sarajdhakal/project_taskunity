# Generated by Django 5.0.6 on 2024-09-11 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_rename_team_members_project_team_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='p1.jpg', upload_to='uploadimages/projects/'),
        ),
    ]
