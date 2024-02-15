from django.urls import path
from . import views as v

urlpatterns = [
    path('all', v.TestListAPIView.as_view()),
    path('<int:pk>', v.TestDetailAPIView.as_view()),

    path('<int:pk>/questions/all', v.QuestionListAPIView.as_view()),
    path('questions/<int:pk>', v.QuestionDetailAPIView.as_view()),

    path('<int:pk>/answers/all', v.AnswerListAPIView.as_view()),
    path('answers/<int:pk>', v.AnswerDetailAPIView.as_view()),
]
