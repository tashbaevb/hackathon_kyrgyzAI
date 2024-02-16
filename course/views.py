import requests

from requests import Response
from rest_framework import generics, status
from .models import LearningProgram, Lesson, Quiz, Sentence
from .serializers import LearningProgramSerializer, LessonSerializer, QuizSerializer, SentenceSerializer

import http.client
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TextToSpeech(APIView):
    def post(self, request):
        text = request.data.get('text')
        if not text:
            return Response({"error": "Text field is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Здесь используйте ваш код для отправки запроса к API TTS
        conn = http.client.HTTPSConnection("http://tts.ulut.kg/api/tts")
        payload = json.dumps({
            "text": text,
            "speaker_id": "1"
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer lfRUZHFlLTht91Fg86AL1sVbcytXBs3vdhp17VTw2XA2a0pM5SAVWOr57KW4f3lL'
        }
        conn.request("POST", "/", payload, headers)
        res = conn.getresponse()
        audio_data = res.read()

        # Возвращаем аудио как ответ
        return Response(audio_data, content_type=res.getheader('Content-Type'))



class LearningProgramListCreate(generics.ListCreateAPIView):
    queryset = LearningProgram.objects.all()
    serializer_class = LearningProgramSerializer


class LessonListCreate(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class QuizListCreate(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class SentenceListCreate(generics.ListCreateAPIView):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer


