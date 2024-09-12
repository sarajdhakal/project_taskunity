# Generated by Django 5.0.6 on 2024-09-12 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_remove_project_user_project_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(default='1.png', upload_to='uploadedimages/users'),
        ),
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(default=1222),
            preserve_default=False,
        ),
    ]