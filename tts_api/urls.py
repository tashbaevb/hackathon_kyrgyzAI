from django.urls import path
from . import views as v

urlpatterns = [
    path('tts/send', v.text_to_speech),
]
