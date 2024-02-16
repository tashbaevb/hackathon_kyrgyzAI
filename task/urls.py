from django.urls import path
from . import views as v

urlpatterns = [
    path('<int:pk>', v.TaskDetailAPIView.as_view()),
]
