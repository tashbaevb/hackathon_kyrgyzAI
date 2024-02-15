from django.db import models

from lesson.models import Lesson


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='tasks')


class Example(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='examples')
