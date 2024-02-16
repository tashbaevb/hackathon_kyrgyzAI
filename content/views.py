from rest_framework import generics

from . import models as m, serializers as s


class BookListAPIView(generics.ListAPIView):
    queryset = m.Book.objects.all()
    serializer_class = s.BookSerializer


class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Book.objects.all()
    serializer_class = s.BookSerializer


class GrammarListAPIView(generics.ListAPIView):
    queryset = m.Grammar.objects.all()
    serializer_class = s.GrammarSerializer


class GrammarDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Grammar.objects.all()
    serializer_class = s.GrammarSerializer


class LessonGrammarListApiView(generics.ListCreateAPIView):
    queryset = m.LessonGrammar.objects.all()
    serializer_class = s.LessonGrammarSerializer
