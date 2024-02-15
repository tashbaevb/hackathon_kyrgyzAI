from django.urls import path
from .views import LearningProgramListCreate, LessonListCreate, QuizListCreate

urlpatterns = [
    path('learning-programs/', LearningProgramListCreate.as_view(), name='learning-programs'),
    path('lessons/', LessonListCreate.as_view(), name='lessons'),
    path('quizzes/', QuizListCreate.as_view(), name='quizzes'),
]
