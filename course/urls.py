from django.urls import path
from .views import CoursePassAPIView, CourseListAPIView, CourseDetailAPIView, MyCourseListAPIView

urlpatterns = [
    path('submit', CoursePassAPIView.as_view()),
    path('all', CourseListAPIView.as_view()),
    path('<int:pk>', CourseDetailAPIView.as_view()),
    path('my', MyCourseListAPIView.as_view()),
]
