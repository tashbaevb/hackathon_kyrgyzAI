from django.urls import path
from . import views as v

urlpatterns = [
    path('submit', v.LessonPassAPIView.as_view()),
    path('<int:pk>', v.LessonDetailAPIView.as_view()),
    path('my', v.MyLessonListAPIView.as_view()),
    path('check', v.LessonCheckAPIView.as_view()),
]
