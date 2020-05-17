from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'article'
