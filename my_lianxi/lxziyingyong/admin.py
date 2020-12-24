from django.contrib import admin
# 从路径 导入 类
from lxziyingyong.models import BookInfo,PeopleInfo
# Register your models here.

# 注册模型
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)