
# 固定写法 最好复制
from django.urls import path
from book.views import index,book,login,weibo

urlpatterns =[
    path('index/',index),


    # 1/100/
    # path('1/100/',book),
    path('<cat_id>/<detail_id>/',book),
    # cat_id =1 <> 符号 占位 这两个用来占位 xxx/xxx/,
    # detail_id = 100

    path('login/',login),

    path('weibo/',weibo),

]


#######################################################3
"""
子应用的urls.py定义
"""
from django.urls import path
from book.views import index,book,login,weibo
urlpatterns = [
    path('index/', index),
    path('<cat_id>/<detail_id>/', book),
    path('login/',login),
    path('weibo/',weibo),
]


























