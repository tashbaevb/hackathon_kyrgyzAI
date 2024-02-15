from rest_framework.response import Response
from rest_framework import generics, permissions

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

        return Response({'message': 'Вы успешно прошли курс'})


class CheckLessonAPIView(generics.CreateAPIView):
    pass


class LessonListAPIView(generics.ListAPIView):
    queryset = m.Lesson.objects.all()
    serializer_class = s.LessonSerializer
    permission_classes = [permissions.IsAuthenticated]


class LessonDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Lesson.objects.all()
    serializer_class = s.LessonSerializer
    permission_classes = [permissions.IsAuthenticated]
