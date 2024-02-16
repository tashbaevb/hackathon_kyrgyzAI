from rest_framework import serializers
from .models import LearningProgram, Lesson, Quiz, Sentence


class LearningProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningProgram
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = '__all__'
