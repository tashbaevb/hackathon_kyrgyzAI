from django.urls import path
from . import views as v

urlpatterns = [
    path('tts/send', v.TTSAPIView.as_view()),
]
