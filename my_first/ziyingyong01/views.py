from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
# Create your views here.

# 1 视图函数的第一个参数 是表示请求实例对象
# request = HttpRequest()

# 2 视图函数必须有响应 返回一个HttpResponse的（子类）实例对象
def index(request):

    # return HttpResponse("this is test page")

    # 定义个字典
    data = {
        'show':'中路水泡子壳一下子'
    }
    # render 加载并渲染html
    # request, 请求对象
    # template_name,  模板名字 写相对路径就可
    # context=None  可以将数据传递给context
    return render(request, 'book/index.html', context=data)