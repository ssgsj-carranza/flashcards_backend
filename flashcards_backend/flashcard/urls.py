from django.urls import path
from . import views

urlpatterns = [
    path('flashcard/', views.FlashcardList.as_view()),
    path('flashcard/<int:pk>/', views.FlashcardDetail.as_view())
]
