from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime # 导入datetime


# 用户信息模型
class UsersModel(models.Model):  #由于数据库中的类都是简短的所以需要更改表名
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    sex = models.IntegerField(default=1)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=50)
    state = models.IntegerField(default=1)
    addtime = models.DateTimeField(default=datetime.now)

    def toDict(self):
        return {'id': self.id, 'username': self.username, 'name': self.name,
                'password': self.password, 'address': self.address,
                'phone': self.phone, 'email': self.email, 'state': self.state}

    class Meta:
        db_table = "users"  # 更改表名
