from django.urls import path
from . import views as v

urlpatterns = [
    path('books/all', v.BookListAPIView.as_view()),
    path('books/<int:pk>', v.BookDetailAPIView.as_view()),
    path('words/all', v.WordListAPIView.as_view()),
    path('words/<int:pk>', v.WordDetailAPIView.as_view()),
    path('sentences/all', v.SentenceListAPIView.as_view()),
    path('sentences/<int:pk>', v.SentenceDetailAPIView.as_view()),
    path('grammar/all', v.GrammarListAPIView.as_view()),
    path('grammar/<int:pk>', v.GrammarDetailAPIView.as_view()),
]
