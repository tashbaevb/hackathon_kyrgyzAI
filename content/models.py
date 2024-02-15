from django.core.validators import FileExtensionValidator
from django.db import models

from main.settings import BOOKS_FOLDER


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(
        upload_to=BOOKS_FOLDER,
        validators=[FileExtensionValidator(
            allowed_extensions=['pdf', 'doc']
        )])


class Word(models.Model):
    title = models.CharField(max_length=150)
    translation = models.CharField(max_length=150)


class Sentence(models.Model):
    text = models.TextField()


class Dictation(models.Model):
    text = models.TextField()


