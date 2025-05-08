from django.db import models
'''
1. Our model class requires to inherit models.Model
2.  The system will automatically add the primary key for us -- id
3.  Field
   field name = model. class(option)
   field name is data programe's  field name
   python,mysql is not suitable in field name
   
   char(M)
   varchar(M)
   M is option
'''
# Create your models here.
class BookInfo(models.Model):
    # id
    name = models.CharField(max_length = 10)

# characters firstly copy
# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)