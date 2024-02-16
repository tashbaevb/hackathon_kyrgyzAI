# Generated by Django 5.0.2 on 2024-02-15 21:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("my_test", "0001_initial"),
        ("task", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="test",
            name="task",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="test",
                to="task.task",
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="test",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="my_test.test",
            ),
        ),
    ]
