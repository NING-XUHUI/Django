from django.db import models


# Create your models here.
# 如果要把一个普通的类变成一个可以映射到数据库中的ORM模型
# 必须要讲父类设置为models.Model或者他的子类
class Book(models.Model):
    # 1. id int类型，自增长
    id = models.AutoField(primary_key=True)
    # 2. name varchar（100）
    name = models.CharField(max_length=100, null=False)
    # 3. author varchar（100）
    author = models.CharField(max_length=100, null=False)
    # 4. price float
    price = models.FloatField(null=False, default=0)


class Publisher(models.Model):
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)

# 1.使用makemigrations生成迁移脚本文件
# python3 manager.py makemigrations

# 2.使用migrate将新生成到迁移脚本文件映射到数据库中
# python3 manager.py migrate
