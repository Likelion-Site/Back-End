from django.urls import path
from answers.views import AnswersList

urlpatterns = [
    path('answers/', AnswersList.as_view()),
]