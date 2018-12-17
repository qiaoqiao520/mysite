from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Question(models.Model):
    question_text = models.CharField('问题内容', max_length=200)
    pub_date = models.DateField('发布时间')

    def __str__(self):  # (了解)控制打印类对象时的输出信息
        return self.question_text

    def was_published_recently(self):
        if timezone.now() - datetime.timedelta(days=1) <= self.pub_date:
            return True
        else:
            return False


class Choice(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('选项内容', max_length=200)
    votes = models.IntegerField('投票数', default=0)

    def __str__(self):
        return self.choice_text


"""
类被翻译成sql执行
create table if not exists question (
    id int primary key autoincrement,
    question_text char(200) comment "问题内容",
    pub_data datetime comment "发布时间"
)

CREATE TABLE if not exists choice (     question_id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    choice_text varchar(200) NOT NULL,    votes integer NOT NULL, 
    id integer NOT NULL REFERENCES question (id) DEFERRABLE INITIALLY DEFERRED);
"""
# Django自带orm框架，用法类似sqlalchemy
# 自定义的类要继承models模型里的Model类，这样orm框架就能把类和数据库联系起来。


