from django.urls import path
from ziyingyong01.views import index
# 子应用中定义子应用的路由
# urlpatterns = [] 固定写法

urlpatterns = [
    # path('index/', index),
    # 第一种
    # path('', index),
    # 第二种
    path('index/', index),
]