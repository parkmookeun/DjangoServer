import json

from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view #함수형 뷰를 만들때 임포트
from rest_framework.views import APIView #클래스형 뷰를 만들때 임포트
from .serializers import AccountSerializer, LoginSerializer
from .models import Account
from .BATuseRSI import Auto, info
# Create your views here.


@api_view(['GET'])
def hello_api(request):
    return Response("Hello Everyone! This is my first APIpage!!!!")


@api_view(['GET', 'POST'])
def sign_up(request):
    if request.method == "GET":
        return Response("This Page is for signup!!!")

    if request.method == "POST":
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def login(request):
    if request.method == "GET":
        return Response("This page is for Login!!!")

    if request.method == "POST":
        info = Account.objects.get(id=request.data['id'])

        if info.password == request.data['password']:
            serializer = LoginSerializer(info)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("Password didn't match with ID!", status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def auto_trade(request):
    if request.method == "GET":
        trade = Auto()
        trade.main()






