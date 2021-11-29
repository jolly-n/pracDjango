import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)  # Charfield : 문자타입
    pub_date = models.DateTimeField('date published')  # DateTimeField : 날짜와 시간타입
    
    def __str__(self):
        return self.question_text
    
    @admin.display(
        boolean=True,  # True, False를 아이콘으로 변경
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        # 버그 수정
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now  # question 생성날짜가 미래로 넘어가지 않도록 현재날짜를 두고 최근기준을 하루로 잡아둠


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Question모델의 질문(question)을 참조한다
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)  # IntegerField : 정수타입

    def __str__(self):
        return self.choice_text
