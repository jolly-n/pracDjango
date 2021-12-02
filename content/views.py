import os
from typing import ContextManager
from django.http import request, response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from uuid import uuid4
from instagram.settings import MEDIA_ROOT
from .models import Feed  # 나와 같은 폴더에 있는 models에 있는 Feed를 사용

# Create your views here.

class Main(APIView):
    def get(self, request):
        # Feed에 있는 모든 데이터를 가져온다
        # order_by('-id') : id값이 큰 것부터 역순으로 가져옴
        feed_list = Feed.objects.all().order_by('-id')

        return render(request, "instagram/main.html", context=dict(feeds=feed_list))

class UploadFeed(APIView):
    def post(self, request):        
        file = request.FILES['file']  # 파일 불러오기

        uuid_name = uuid4().hex  # 저장되는 이미지 파일의 이름에 고유한 랜덤 id값을 준다
        save_path = os.path.join(MEDIA_ROOT, uuid_name)  

        with open(save_path, 'wb+') as destination:  # 실제로 파일을 저장해주는 부분
            for chunk in file.chunks():
                destination.write(chunk)
        
        image = uuid_name  
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile = request.data.get('profile')

        # 피드를 만들어주기
        Feed.objects.create(image=image, content=content, user_id=user_id, profile=profile, like_count=0)

        return Response(status=200)