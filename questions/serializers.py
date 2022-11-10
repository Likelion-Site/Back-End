from rest_framework import serializers
from answers.serializers import AnswerSerializer
from questions.models import Question


class QuesetionSerializer(serializers.ModelSerializer) :
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta :
        model = Question
        fields = ['id','question','answers']
        # fields = ['id','question']
