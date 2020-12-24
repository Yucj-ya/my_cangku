from django.shortcuts import render
# 得有响应
from django.http.response import HttpResponse
# Create your views here.
# 设定网址为index
def index(request):
    # 返回的东西
    return HttpResponse('this is test page')