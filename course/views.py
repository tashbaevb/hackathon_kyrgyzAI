from rest_framework import generics
from .models import LearningProgram, Lesson, Quiz
from .serializers import LearningProgramSerializer, LessonSerializer, QuizSerializer


class LearningProgramListCreate(generics.ListCreateAPIView):
    queryset = LearningProgram.objects.all()
    serializer_class = LearningProgramSerializer


class LessonListCreate(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class QuizListCreate(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
