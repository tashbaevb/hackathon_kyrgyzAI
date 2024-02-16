from django.urls import path

from . import views as v
from lesson import views as lv

urlpatterns = [
    path('submit', v.CoursePassAPIView.as_view()),
    path('all', v.CourseListAPIView.as_view()),
    path('<int:pk>', v.CourseDetailAPIView.as_view()),
    path('<int:pk>/lessons', lv.LessonListAPIView.as_view()),
    path('my', v.MyCourseListAPIView.as_view()),
]
