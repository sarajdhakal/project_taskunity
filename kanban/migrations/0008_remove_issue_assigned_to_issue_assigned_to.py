# Generated by Django 5.0.6 on 2024-09-12 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0007_issue_due_date'),
        ('projects', '0012_remove_project_user_project_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='assigned_to',
        ),
        migrations.AddField(
            model_name='issue',
            name='assigned_to',
            field=models.ManyToManyField(blank=True, to='projects.employee'),
        ),
    ]
