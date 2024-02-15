from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    LEVEL = (
        ('Начинающий', 'Начинающий'),
        ('Средний', 'Средний'),
        ('Продвинутый', 'Продвинутый'),
    )
    level = models.CharField(max_length=100, choices=LEVEL)
    title = models.CharField(max_length=150)
    description = models.TextField()


class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrolled_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrolled_users')

