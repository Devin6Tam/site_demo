from django.db import models
from django.utils import timezone
import datetime
import uuid
"""
一个模型（model）就是一个单独的、确定的数据的信息源，包含了数据的字段和操作方法。通常，每个模型映射为一张数据库中的表。

基本的原则如下：

每个模型在Django中的存在形式为一个Python类
每个模型都是django.db.models.Model的子类
模型的每个字段（属性）代表数据表的某一列
Django将自动为你生成数据库访问API
"""
# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Question(models.Model):
    #id 一般采用默认id生成策略不要指定，如若需要指定生成，则需要参考如下操作
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question_text = models.CharField(max_length=200)
    questioner = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    # 是否最近发布
    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    # 输出打印信息
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 limit_choices_to={'is_staff': True},
                                 )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # 输出打印信息
    def __str__(self):
        return self.choice_text