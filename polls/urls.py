from django.urls import path

from . import views

app_name = 'polls'  # 해당 앱에서 사용하는 url에 대해 이름을 명시해줌
urlpatterns = [  # view를 호출하기 위한 url코드 작성
    # ex: /polls/
    path('', views.index, name='index'),  # 해당주소(/polls)로 index view가 호출 된다.
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]