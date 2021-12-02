from django.db import models

# Create your models here.
class Feed(models.Model):  # Feed라는 객체의 데이터베이스 만들기
    profile    = models.TextField()  # 프로필사진    
    user_id    = models.TextField()  # 사용자아이디
    image      = models.TextField()  # 사진
    content    = models.TextField()  # 글내용
    like_count = models.IntegerField()  # 좋아요수