from django.urls import path
from questions.views import QuestionList,QuestionDetail

urlpatterns = [
    path('questions/',QuestionList.as_view()),
    path('questions/<int:pk>', QuestionDetail.as_view())
]