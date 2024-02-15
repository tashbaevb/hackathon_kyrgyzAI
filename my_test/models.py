from django.db import models

from task.models import Task


class Test(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='test')


class Question(models.Model):
    title = models.CharField(max_length=255)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')


class Answer(models.Model):
    title = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

