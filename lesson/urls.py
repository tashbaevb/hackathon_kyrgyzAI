from django.urls import path

from . import views as v

urlpatterns = [
    path('submit', v.LessonPassAPIView.as_view()),
    path('<int:pk>', v.LessonDetailAPIView.as_view()),
    path('<int:pk>/questions', v.QuestionListAPIView.as_view()),
    path('<int:pk>/examples', v.ExampleListAPIView.as_view()),
    path('my', v.MyLessonListAPIView.as_view()),
    path('check', v.LessonCheckAPIView.as_view()),
    path('api/translate/', v.TranslateGrammarListApiView.as_view(), name='translate-list'),
    path('api/translate/<int:pk>/text-to-speech/', v.text_to_speech_diktovka, name='text-to-speech'),
]
