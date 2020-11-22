import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Book(models.Model):
    class Meta(object):
        db_table = 'book'
    title = models.CharField(verbose_name='タイトル', max_length=255)
    image = models.ImageField(verbose_name='画像', null=True, blank=True)

# class CustomUser(AbstractUser):
#     class Meta:
#         db_table ='custom_user'
#     login_count = models.IntegerField(verbose_name='ログイン回数', default=0)
