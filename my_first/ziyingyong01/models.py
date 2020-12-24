from django.db import models

# Create your models here.
# 准备书籍列表信息的模型类
class BookInfo(models.Model):
    # 创建字段，字段类型
    name = models.CharField(max_length=10)

    def __str__(self):
        # 将模型类以字符串方式输出
        return self.name


class PersonInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键：人物属于哪本书 on_delete 外键的级联关系 
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name