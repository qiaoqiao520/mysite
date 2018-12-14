from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField('问题内容', max_length=200)
    pub_data = models.DateField('发布时间')


class Choice(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('选项内容', max_length=200)
    votes = models.IntegerField('投票数', default=0)


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


