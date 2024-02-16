from django.urls import path
from . import views as v

urlpatterns = [
    path("lesson/grammar/", v.LessonGrammarListApiView.as_view()),
    path("books/all/", v.BookListAPIView.as_view(), name='book-list'),
    path("books/<int:pk>/", v.BookDetailAPIView.as_view(), name="book-detail"),
    path("grammar/all", v.GrammarListAPIView.as_view(), name='grammar-list'),
    path("grammar/<int:pk>/", v.GrammarDetailAPIView.as_view(), name="grammar-detail"),
]
