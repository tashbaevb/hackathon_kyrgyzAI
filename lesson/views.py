from rest_framework.response import Response
from rest_framework import generics, permissions, views

from . import models as m, serializers as s


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
    queryset = m.Lesson.objects.all()
    serializer_class = s.LessonSerializer
    permission_classes = [permissions.IsAuthenticated]


class LessonDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Lesson.objects.all()
    serializer_class = s.LessonSerializer
    permission_classes = [permissions.IsAuthenticated]
