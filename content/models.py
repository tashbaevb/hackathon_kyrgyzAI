from django.core.validators import FileExtensionValidator
from django.db import models

from main.settings import BOOKS_FOLDER, BOOK_IMAGE_FOLDER


class Book(models.Model):
    author = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField(null=True)
    image = models.ImageField(upload_to=BOOK_IMAGE_FOLDER)


class Grammar(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    example = models.TextField()
    note = models.TextField(null=True, blank=True)
