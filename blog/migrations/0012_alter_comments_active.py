# Generated by Django 4.1.5 on 2023-01-29 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_article_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]