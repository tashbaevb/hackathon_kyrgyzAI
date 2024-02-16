from django.urls import path
from . import views as v

urlpatterns = [
    path('all', v.TaskListAPIView.as_view()),
    path('<int:pk>', v.TaskDetailAPIView.as_view()),
]
