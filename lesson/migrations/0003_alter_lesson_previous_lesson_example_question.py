# Generated by Django 5.0.2 on 2024-02-16 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_lesson_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='previous_lesson',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_lesson', to='lesson.lesson'),
        ),
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examples', to='lesson.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('correct_answer', models.CharField(max_length=150)),
                ('answer_1', models.CharField(max_length=150)),
                ('answer_2', models.CharField(max_length=150)),
                ('explanation', models.TextField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='lesson.lesson')),
            ],
        ),
    ]