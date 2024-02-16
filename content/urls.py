from django.urls import path
from . import views as v

urlpatterns = [
    path("lesson/grammar/", v.LessonGrammarListApiView.as_view()),
    path("books/", v.BookListAPIView.as_view(), name='book-list'),
    path("books/<int:pk>/", v.BookDetailAPIView.as_view(), name="book-detail"),
    path("grammar/", v.GrammarListAPIView.as_view(), name='grammar-list'),
    path("grammar/<int:pk>/", v.GrammarDetailAPIView.as_view(), name="grammar-detail"),
    path("word/", v.WordListAPIView.as_view(), name='word-list'),
    path("word/<int:pk>/", v.WordDetailAPIView.as_view(), name="word-detail"),
    path("sentence/", v.SentenceListAPIView.as_view(), name='sentence-list'),
    path("sentence/<int:pk>/", v.SentenceDetailAPIView.as_view(), name="sentence-detail"),
]
