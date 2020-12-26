from django.shortcuts import render
from django.http.response import HttpResponse
from book.models import BookInfo,PeopelInfo
# Create your views here.
def index(request):

    BookInfo.objects.all()

    return HttpResponse('ok')

#########################
# 新增
# 导入
from book.models import BookInfo
# 创建一个实例对象
book=BookInfo()
# 属性
book.name='django'
book.readcount=10
book.commentcount=100
book.pub_date='2000-2-2'
# 手动调用sava
book.save()

# 方法2
new_book=BookInfo.objects.create(
    name='ppython',
    pub_date='2020-1-1',
    readcount=10,
    commentcount=100
)

#############
# 修改
# 获取实例对象
# bookinfo.objects.get(id=1) -- select * from bookinfo where id=1
book = BookInfo.objects.get(id=1)
# 通过修改实例对象的属性来修改数据
book.name='射雕英雄后传'
# book.save() 人为调用
book.save()

# 第二种 直接调用 查询数据的方法 查询之后直接调用update方法
# filter() 根据
BookInfo.objects.filter(id=1).update(
    name='射雕小英雄'
)

##############
# 删除
book = BookInfo.objects.get(id=5)
book.delete()
# 第二种
BookInfo.objects.filter(id=6).delete()

############
# 查询
BookInfo.objects.get(id=1)
# 查询所有
BookInfo.objects.all()
# 查询数量
BookInfo.objects.all().count()