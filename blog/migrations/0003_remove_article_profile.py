# Generated by Django 4.1.5 on 2023-01-07 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_userprofile_favourite_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='profile',
        ),
    ]
