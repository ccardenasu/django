# Generated by Django 4.2 on 2024-07-24 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='year',
            field=models.TextField(max_length=4, null=True),
        ),
    ]
