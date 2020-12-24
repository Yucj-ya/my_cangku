from django.db import models

# Create your models here.
# 定义书籍类
class BookInfo(models.Model):
    # 字段名字 最大10位
    name = models.CharField(max_length=10)

    # 运行类自动以字符串显示输出
    def __str__(self):
        return self.name

# 定义人类
class PeopleInfo(models.Model):
    # 名字 性别 book的外键
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

