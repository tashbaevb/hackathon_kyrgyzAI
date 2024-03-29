# Generated by Django 5.0.2 on 2024-02-16 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('content', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='image/books/')),
            ],
        ),
        migrations.CreateModel(
            name='Grammar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('example', models.TextField()),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LessonGrammar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('example', models.TextField()),
                ('note', models.TextField()),
            ],
        ),
    ]
