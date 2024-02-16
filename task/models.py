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


class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=150)
    correct_answer = models.CharField(max_length=150)
    answer_1 = models.CharField(max_length=150)
    answer_2 = models.CharField(max_length=150)
    explanation = models.TextField()