from django.db import models

LANGUAGE_LEVEL = (
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced')
)


class LearningProgram(models.Model):
    level = models.CharField(max_length=20, choices=LANGUAGE_LEVEL, blank=True, default='Beginner')
    description = models.TextField()

    def __str__(self):
        return f"{self.level} Program"


class Lesson(models.Model):
    program = models.ForeignKey(LearningProgram, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=250)
    explanation = models.TextField()

    def __str__(self):
        return self.question
