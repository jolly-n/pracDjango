import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)  # Charfield : 문자타입
    pub_date = models.DateTimeField('date published')  # DateTimeField : 날짜와 시간타입
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Question모델의 질문(question)을 참조한다
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)  # IntegerField : 정수타입

    def __str__(self):
        return self.choice_text
