from django.urls import path
from .views import UploadFeed 

# content의 urls 분리하기
urlpatterns = [
    path('upload', UploadFeed.as_view())
]