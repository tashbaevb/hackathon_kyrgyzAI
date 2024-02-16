from django.core.validators import FileExtensionValidator
from django.db import models

from main.settings import BOOKS_FOLDER, BOOK_IMAGE_FOLDER


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=BOOK_IMAGE_FOLDER)
    file = models.FileField(
        upload_to=BOOKS_FOLDER,
        validators=[FileExtensionValidator(
            allowed_extensions=['pdf', 'doc']
        )])


class Grammar(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    example = models.TextField()
    note = models.TextField(null=True, blank=True)


class LessonGrammar(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    example = models.TextField()
    note = models.TextField()
