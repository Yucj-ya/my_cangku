from django.shortcuts import render
from django.http.response import HttpResponse

import json


# Create your views here.

def index(request):
    page = request.GET.get('page', 1)

    context = {

    }

    """
    获取json数据
    body = request.body
    body_str = body.decode()
    body_dict = json.loads(body_str)
    print(body_dict)
    """
    # 再验证 from-data
    print(request.POST)
    return render(request, 'index.html', context=context)


"""
面向对象--类

"""


# 面向过程--函数
# 视图函数
def test(request):
    # 查看获取的请求类型
    # print(request.method)
    # 根据不同的 请求方式 来区分
    # 去实现不同的业务逻辑
    if request.method == 'GET':
        return HttpResponse('get')
    else:
        return HttpResponse('post')

    # return HttpResponse("test")


# 面向对象 -- 类
# 类 除了属性就是方法

"""
class 类名（）：
    方法名
    def get():
        pass

    def post():
        pass

类视图的定义
1 类视图继承自 view
2 类视图的方法 -- 根据请求方式来实现的
    如用 post 发送了一个 get 请求 我们就实现类视图中的 get 方法
    如用 post 发送了一个 post 请求 我们就实现类视图中的 post 方法

"""
from django.views import View


class JDLogin(View):  # 继承自view

    # self 指的是实例对象
    # request 指的是请求对象
    def get(self, request):
        return HttpResponse('jd - login - get')

    def post(self, request):
        # self abc(request) 间接调用
        return HttpResponse('jd - login - post')

    # 访问不到
    # 不能直接调用 self.abc
    def abc(self, request):
        return HttpResponse('abc')


####################面向对象回顾#################################

class Person(object):
    # 方法
    # 实力方法
    def say(selfs):
        pass

    # 类方法
    @classmethod
    def eat(cls):
        pass

    # 静态方法
    @staticmethod
    def run():
        pass


# p = Person()
# p.say()
#
# # cls
# Person.eat()
#
# # static
# Person.run()

############################################
"""
如果访问个人中心页面 必须要求用户登录

1 定义个人中心视图
2 必须要求用户登录

"""

# 可以使用装饰器
# 还可以使用多继承！！！

# class CenterView(View):
#     def get(self, request):
#         isLogin = False
#         if isLogin:
#             # 展示个人信息
#             return HttpResponse('center get')
#         else:
#             return HttpResponse('请登录')
#
#     def post(self, request):
#         isLogin = False
#         if isLogin:
#             return HttpResponse('center post')
#         else:
#             return HttpResponse('请登录')


# 系统有一个类 可以帮助我们进行是否登录的判断LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

# LoginRequiredMixin
# LoginRequiredMixin    继承自AccessMixin
# AccessMixin 继承了object

# CenterView 不能直接继承LoginRequiredMixin

# CenterView 要求既要继承view 又继承LoginRequirdeMixin

# class CenterView(View,LoginRequiredMixin):    方法1
# class CenterView(LoginRequiredMixin,View):    方法2

# View 有一个 dispath
# LoginRequirdeMixin 也有一个 dispath

# 想 先验证是否登录 如登录正常执行 如没登录 跳转值登录
# 结论 应该先走 LoginRequiredMixin 的dispath

# class CenterView(View,LoginRequiredMixin):    方法1
"""
mro
(<class 'book.views.CenterView'>, <class 'django.views.generic.base.View'>, <class 'django.contrib.auth.mixins.LoginRequiredMixin'>, <class 'django.contrib.auth.mixins.AccessMixin'>, <class 'object'>)

"""
# class CenterView(LoginRequiredMixin,View):    方法2
"""
mro
(<class 'book.views.CenterView'>, <class 'django.contrib.auth.mixins.LoginRequiredMixin'>, <class 'django.contrib.auth.mixins.AccessMixin'>, <class 'django.views.generic.base.View'>, <class 'object'>)

"""


# 打印 mro顺序

from django.contrib.auth.mixins import LoginRequiredMixin

# class CenterView(View,LoginRequiredMixin):
class CenterView(LoginRequiredMixin,View):
# class CenterView(View):
    def get(self,request):

        # 展示个人信息
        return HttpResponse('center get')


    def post(self,request):

        # 修改个人信息
        return HttpResponse('center post')


from django.contrib.auth.mixins import LoginRequiredMixin

# LoginRequiredMixin 继承自AccessMixin
# AccessMixin 继承了object
# CenterView 不能直接继承LoginRequiredMixin
# CenterView 要求既要继承view 又继承LoginRequirdeMixin

# class CenterView(View,LoginRequiredMixin): 方法1
# class CenterView(LoginRequiredMixin,View): 方法2

# View 有个 dispath
# LoginRequiredMixin 也有一个dispath


# 应该先验证是否登录 如登录了 正常访问 如果没登录则跳转登录页面
#  所以 应该先走Lxxx 的 dispath 方法


# 打印mro的顺序 __MRO__

# from django.contrib.auth.mixins import LoginRequiredMixin
#
#
# # class CenterView(View, LoginRequiredMixin):
# class CenterView(LoginRequiredMixin, View):
#     # class CenterView(view):
#     def get(self, request):
#         # 展示个人信息
#         return HttpResponse('center get')
#
#     def post(self, request):
#         # 修改个人信息
#         return HttpResponse('center.post')

#####################################################################

# def test(request):
#
#     return HttpResponse("test")
