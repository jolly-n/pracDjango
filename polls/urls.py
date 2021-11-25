from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),  # views로 넘겨줌
]