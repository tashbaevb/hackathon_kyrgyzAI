# Generated by Django 5.0.2 on 2024-02-16 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='image',
            field=models.ImageField(null=True, upload_to='image/lessons/'),
        ),
    ]
