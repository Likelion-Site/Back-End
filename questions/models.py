from django.db import models

class Question(models.Model) :
    question = models.TextField()
    # question = models.CharField(max_length=300)