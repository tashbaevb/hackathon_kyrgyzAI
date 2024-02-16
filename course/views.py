from rest_framework.response import Response
from rest_framework import generics, permissions

from . import models as m, serializers as s


class MyCourseListAPIView(generics.ListAPIView):
    queryset = m.UserCourse.objects.all()
    serializer_class = s.UserCourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class CoursePassAPIView(generics.CreateAPIView):
    serializer_class = s.UserCourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        data['user'] = user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'Вы успешно прошли курс'})


class CourseListAPIView(generics.ListAPIView):
    queryset = m.Course.objects.all()
    serializer_class = s.CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Course.objects.all()
    serializer_class = s.CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
