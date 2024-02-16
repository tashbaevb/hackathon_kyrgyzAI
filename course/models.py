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
    incorrect_answer1 = models.CharField(max_length=250)
    incorrect_answer2 = models.CharField(max_length=250)
    explanation = models.TextField()

    def __str__(self):
        return self.question


class Word(models.Model):
    title = models.CharField(max_length=150)
    translation = models.CharField(max_length=150)


class Sentence(models.Model):
    text = models.TextField()
    audio_url = models.URLField(blank=True, null=True)  # Поле для хранения ссылки на аудио



class Dictation(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
