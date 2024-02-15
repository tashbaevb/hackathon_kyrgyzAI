from django.urls import path
from . import views as v

urlpatterns = [
    path('submit', v.CoursePassAPIView.as_view()),
    path('all', v.CourseListAPIView.as_view()),
    path('<int:pk>', v.CourseDetailAPIView.as_view()),
    path('my', v.MyCourseListAPIView.as_view()),
]
