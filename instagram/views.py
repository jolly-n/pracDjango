from django.shortcuts import render
from rest_framework.views import APIView

class First(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, "instagram/main.html")

    def post(self, request):
        # print("post로 호출")
        return render(request, "instagram/main.html")