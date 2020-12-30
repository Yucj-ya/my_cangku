from django.urls import path
from book.views import index, test
from book.views import JDLogin, CenterView

urlpatterns = [
    path('index/', index),
    # 视图函数
    path('test/', test),

    ###########################
    # 类视图的url
    # path 的第一个参数 url
    # path 的第二个参数 视图函数的名字

    # JDlogin 类名
    # 先记住写法 -- 一会重点讲第二个参数
    path('jd/', JDLogin.as_view()),

    # 个人中心 path
    path('center/', CenterView.as_view()),

]

######################################################

