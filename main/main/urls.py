from django.contrib import admin
from django.urls import path
from rest_framework.decorators import APIView
from rest_framework.response import Response

class get_data(APIView):
    def get(self,request):
        data={
            "message":"you invoked my callback"
        }
        return Response(data)
    def post(self,request):
        data=request.data
        print(data)
        return Response(data)
urlpatterns = [
    path('',get_data.as_view())
]
