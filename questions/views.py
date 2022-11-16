from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from questions.serializers import QuesetionSerializer
from questions.models import Question

class QuestionList(APIView) :
    def get(self, request, format=None) :
        questions = Question.objects.all()
        serializer = QuesetionSerializer(questions, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None) :
        serializer = QuesetionSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionDetail(APIView) :
    def get_object(self, pk) :
        try :
            return Question.objects.get(pk=pk)
        except :
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk, format=None) :
        question = self.get_object(pk)
        serializer = QuesetionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None) :
        question = self.get_object(pk)
        serializer = QuesetionSerializer(question, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None) :
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)