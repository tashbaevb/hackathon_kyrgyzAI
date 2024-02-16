from django.db import models

from account.models import User
from course.models import Course


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    previous_lesson = models.OneToOneField('self', on_delete=models.CASCADE, related_name='next_lesson')


class UserLesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lessons')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='users')


class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=150)
    correct_answer = models.CharField(max_length=150)
    answer_1 = models.CharField(max_length=150)
    answer_2 = models.CharField(max_length=150)
    explanation = models.TextField()
