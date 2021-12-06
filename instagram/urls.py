"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

from instagram.views import First
from content.views import Main, UploadFeed  # content폴더에 views파일에 있는 Main, UploadFeed를 사용

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', Main.as_view()),
    path('content/', include('content.urls')),  # content 앱에 있는 url 연결하기
    path('user/', include('user.urls')),  # user 앱에 있는 url 연결하기
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)