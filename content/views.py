from rest_framework import permissions, generics

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
