from rest_framework.response import Response
from rest_framework import generics, permissions, views, status
import requests
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from pydub import AudioSegment

from . import models as m, serializers as s
from .models import Translate


class MyLessonListAPIView(generics.ListAPIView):
    queryset = m.UserLesson.objects.all()
    serializer_class = s.UserLessonSerializer
    permission_classes = [permissions.IsAuthenticated]


class LessonPassAPIView(generics.CreateAPIView):
    serializer_class = s.UserLessonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'Вы успешно прошли урок'})


class LessonCheckAPIView(views.APIView):

    def post(self, request, *args, **kwargs):
        lesson = m.Lesson.objects.filter(request.data['id'])
        return m.UserLesson.objects.get(user=request.user, lesson=lesson.previous_lesson).exists()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = s.LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        course_id = self.kwargs.get('pk')
        return m.Lesson.objects.filter(course_id=course_id)


class LessonDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Lesson.objects.all()
    serializer_class = s.LessonSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExampleListAPIView(generics.ListAPIView):
    serializer_class = s.ExampleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return m.Example.objects.filter(lesson_id=pk)


class ExampleDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Example.objects.all()
    serializer_class = s.ExampleSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionListAPIView(generics.ListAPIView):
    serializer_class = s.QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return m.Question.objects.filter(lesson_id=pk)


class TranslateGrammarListApiView(generics.ListCreateAPIView):
    queryset = m.Translate.objects.all()
    serializer_class = s.TranslateSerializer


@api_view(['POST'])
def text_to_speech_diktovka(request, pk):
    translate_object = get_object_or_404(Translate, pk=pk)

    data = {
        'text': translate_object.text,
        'speaker_id': 1,
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer lfRUZHFlLTht91Fg86AL1sVbcytXBs3vdhp17VTw2XA2a0pM5SAVWOr57KW4f3lL'
    }
    response = requests.post('http://tts.ulut.kg/api/tts', json=data, headers=headers)

    if response.status_code != 200:
        return Response({'error': 'Ошибка при отправке данных на другой backend'}, status=response.status_code)

    if 'audio' in response.headers.get('Content-Type', ''):
        audio_data = response.content
        return HttpResponse(audio_data, content_type=response.headers['Content-Type'])

    return Response(response.json(), status=status.HTTP_200_OK)
