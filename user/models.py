from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser  # 장고에서 기본적으로 제공하는 base_user를 가져옴

# Create your models here.
class User(AbstractBaseUser):
    """
        유저 프로필 사진
        유저 닉네임        -> 화면에 표기되는 이름
        유저 이름          -> 실제 사용자 이름
        유저 이메일 주소   -> 회원가입할 때 사용되는 아이디
        유저 비밀번호      -> 기본값 쓰자
    """

    profile = models.TextField()  # 프로필사진
    nickname = models.CharField(max_length=24, unique=True)  # 닉네임
    name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'nickname'

    class Meta:  # user_User(앱이름_클래스이름)가 아닌 원하는 테이블이름 만들어 주기
        db_table = "User"