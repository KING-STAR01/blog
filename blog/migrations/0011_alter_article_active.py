# Generated by Django 4.1.5 on 2023-01-29 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_comments_active_comments_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
