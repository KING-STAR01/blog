# Generated by Django 4.1.5 on 2023-01-20 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_userprofile_my_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='my_posts',
        ),
    ]
