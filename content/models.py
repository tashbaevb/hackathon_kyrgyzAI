from django.core.validators import FileExtensionValidator
from django.db import models

from main.settings import BOOKS_FOLDER, IMAGE_FOLDER


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=IMAGE_FOLDER)
    file = models.FileField(
        upload_to=BOOKS_FOLDER,
        validators=[FileExtensionValidator(
            allowed_extensions=['pdf', 'doc']
        )])

    class Meta:
        db_table = 'books'
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title

class Grammar(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    example = models.TextField()
    note = models.TextField(null=True, blank=True)


class Word(models.Model):
    title = models.CharField(max_length=150)
    translation = models.CharField(max_length=150)


class Sentence(models.Model):
    text = models.TextField()


class Dictation(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
