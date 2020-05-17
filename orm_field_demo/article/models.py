from django.db import models


# Create your models here.
class Article(models.Model):
    # 如果想用自己定义的field作为主键，必须设置primarykey为true
    id = models.BigAutoField(primary_key=True)
    # 如果没有指定null=True，默认为False
    # 如果想要使用null，使用NullBooleanField
    removed = models.NullBooleanField()
