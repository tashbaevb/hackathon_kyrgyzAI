from django.urls import path
from . import views as v

urlpatterns = [
    path('send', v.text_to_speech),
]
