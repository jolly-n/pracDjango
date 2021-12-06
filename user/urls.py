from django.urls import path
from .views import Join, Login

# user의 urls 분리하기
urlpatterns = [
    path('join', Join.as_view()),
    path('login', Login.as_view())
]