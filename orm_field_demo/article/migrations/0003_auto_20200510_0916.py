# Generated by Django 3.0.5 on 2020-05-10 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_removed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='removed',
            field=models.NullBooleanField(),
        ),
    ]