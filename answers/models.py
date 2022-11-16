from django.db import models
from questions.models import Question

# Create your models here.
class Answer(models.Model) :
    content = models.TextField(verbose_name='답변')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name='작성시간')
    
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, related_name='answers')
    