from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
from django.http.request import HttpRequest

# 视图函数

def index(request):

    return HttpResponse('登录')


###########################333
# http://127.0.0.1:8000/书籍大类/书籍id

def book(request,cat_id,detail_id):
    # print(cat_id,detail_id)
    return HttpResponse('喜欢看书')

###################################################3
    # 获取查询字符串 搜索 分页时用到
    # 获取查询字符串所有数据 request.GET
    query_string =request.GET
    # print(query_string)
    # < QueryDict: {'a': ['10'], 'b': ['20']} >

    # 获取查询字符串的指定数据
    # a = query_string['a']
    # b = query_string.get('b')
    # print(a,b)

    """
     普通字典 键值对 一键一值
    querydict 
    可以一键一值 也可以一键多值
    一键一值：   QueryDict_data.get(key)
    一键多值：   QueryDict_data.getlist(key)
    
    """
    # alist = query_string.getlist('a')
    # b = query_string.get('b')
    # print(alist,b)


    # 非常规使用
    # get和getlist反着用 也会获取数据 但是会数据丢失
    # get剩最后一个数据
    # getlist 得到列表

    """
    get(key,key对应的数据不存在使用默认值)
    """
    # page=query_string.get('page',1)
    # print(page)
    return HttpResponse('喜欢看书')
    #

def login(request):


   # POST请求
   # 接收form-data 数据的属性
    body = request.POST
    print(body)


    return HttpResponse('login')


def weibo(request):


    # json接受的数据的接受是在 request.body中
    # 接受参数
    body = request.body
    # print(body)

    # 讲bytes类型数据转换成str类型
    # 不是字典
    # 是json格式的字符串
    body_str = body.decode()
    # print(body_str)

    import json
    data = json.loads(body_str)

    print(data)
    return HttpResponse('weibo json')

############################################################################
"""
http://ip:port/uri/?key=value&key2=value2
以问好（？）为分隔符
？前边为我们访问的url http://ip:port/uri/
?后边为查询字符串 key=value&key2=value2
查询字符串是以 & 作为分隔的

http://127.0.0.1:8000/1/100/?a=10&b=20
"""
def book(request,cat_id,detail_id):
    # 获取查询字符串所有数据
    query_string = request.GET
    # 获取查询字符串的制定数据
    a = query_string['a']
    b = query_string['b']
    print(a,b)

    return HttpResponse('giao')


def book(request,cat_id,detail_id):
    query_string = request.GET
    a = query_string['a']
    b = query_string['b']
    print(a,b)

    return HttpResponse('sa')

"""
http://127.0.0.1:8000/1/100/?a=10&b=20&a=666
QueryDict 可以 一键一值 也可以一键多值 
一键一值 : QueryDict_data.get(key) 
一键多值 : QueryDict_data.getlist(key) liebiao
"""
def book(request,cat_id,detail_id):
    query_string = request.GET
    alist = query_string.getlist('a')
    b = query_string.get('b')
    print(alist,b)

def book(request,cat_id,detail_id):
    query_string = request.GET
    alist = query_string.getlist('a')
    b = query_string.get('b')
    print(alist,b)

"""
get 可以添加默认值 .get('xxx',1)
"""
def book(request,cat_id,detail_id):
    query_string = request.GET
    page = query_string.get('page',2)
    print(page)

"""
127.0.0.1:8000/login/

"""
def login(request):

    return HttpResponse('login')

############################################3
"""
post请求 表单类型 form data
"""
def login(request):
    # 接收form-data 数据的属性
    body = request.POST
    print(body)

    return HttpResponse('dsf')

"""
非标单类型 non-form-data
postman 发送json 数据
"""
def weibo (request):
    # 接收参数
    body = request.body
    # bytes类型数据转换为str类型 解码
    body_str = body.decode()
    # 讲json形式字符串转换位字典
    import json
    data = json.loads(body_str)
    print(data)

    return HttpResponse('df')























