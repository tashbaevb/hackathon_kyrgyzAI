from django.urls import path
from .views import LearningProgramListCreate, LessonListCreate, QuizListCreate, SentenceListCreate, TextToSpeech

urlpatterns = [
    path('learning-programs/', LearningProgramListCreate.as_view(), name='learning-programs'),
    path('lessons/', LessonListCreate.as_view(), name='lessons'),
    path('quizzes/', QuizListCreate.as_view(), name='quizzes'),
    path('sentences/', SentenceListCreate.as_view(), name='sentence-list-create'),
    path('text-to-speech/', TextToSpeech.as_view(), name='text-to-speech'),
]
