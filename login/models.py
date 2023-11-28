from django.db import models
from django.contrib.auth.models import *

# Create your models here.

#사실상 안 씀

#class Users(models.Model):
#    username = models.CharField(max_length=20,verbose_name="사용자학번")
#    password = models.CharField(max_length=20, verbose_name="비밀번호")
#    registered_dttm = models.DateField(auto_now_add=True, verbose_name="등록시간")
#
#    def __str__(self):
#        return self.username
#
#    class Meta:
#        db_table = "users"
#        verbose_name ="사용자"
#        verbose_name_plural = "사용자"