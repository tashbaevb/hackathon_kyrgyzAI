from rest_framework.response import Response
from rest_framework import permissions, generics, status, views

from . import models as m, serializers as s


class BookListAPIView(generics.ListAPIView):
    queryset = m.Book.objects.all()
    serializer_class = s.BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Book.objects.all()
    serializer_class = s.BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class GrammarListAPIView(generics.ListAPIView):
    queryset = m.Grammar.objects.all()
    serializer_class = s.GrammarSerializer
    permission_classes = [permissions.IsAuthenticated]


class GrammarDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Grammar.objects.all()
    serializer_class = s.GrammarSerializer
    permission_classes = [permissions.IsAuthenticated]


class WordListAPIView(generics.ListAPIView):
    queryset = m.Word.objects.all()
    serializer_class = s.WordSerializer
    permission_classes = [permissions.IsAuthenticated]


class WordDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Word.objects.all()
    serializer_class = s.WordSerializer
    permission_classes = [permissions.IsAuthenticated]


class SentenceListAPIView(generics.ListAPIView):
    queryset = m.Sentence.objects.all()
    serializer_class = s.SentenceSerializer
    permission_classes = [permissions.IsAuthenticated]


class SentenceDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Sentence.objects.all()
    serializer_class = s.SentenceSerializer
    permission_classes = [permissions.IsAuthenticated]


class DictationListAPIView(generics.ListAPIView):
    queryset = m.Dictation.objects.all()
    serializer_class = s.DictationSerializer
    permission_classes = [permissions.IsAuthenticated]


class DictationDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Dictation.objects.all()
    serializer_class = s.DictationSerializer
    permission_classes = [permissions.IsAuthenticated]

