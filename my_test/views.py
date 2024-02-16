from rest_framework.response import Response
from rest_framework import generics, permissions

from . import models as m, serializers as s


class TestListAPIView(generics.ListAPIView):
    queryset = m.Test.objects.all()
    serializer_class = s.TestSerializer
    permission_classes = [permissions.IsAuthenticated]


class TestDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Test.objects.all()
    serializer_class = s.TestSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionListAPIView(generics.ListAPIView):
    serializer_class = s.QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return m.Question.objects.filter(pk=pk)


class QuestionDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Question.objects.all()
    serializer_class = s.QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class AnswerListAPIView(generics.ListAPIView):
    queryset = m.Answer.objects.all()
    serializer_class = s.AnswerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return m.Answer.objects.filter(pk=pk)


class AnswerDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Answer.objects.all()
    serializer_class = s.AnswerSerializer
    permission_classes = [permissions.IsAuthenticated]
