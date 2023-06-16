from django.db import models


# Create your models here.

# class Users(models.Model):
#     """用户表"""
#
#     gender = (
#         ('male', '男'),
#         ('female', '女')
#     )
#
#     name = models.CharField(max_length=128, unique=True)
#     password = models.CharField(max_length=256)
#     email = models.EmailField(unique=True)
#     sex = models.CharField(max_length=32, choices=gender, default='男')
#     c_time = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         ordering = ['c_time']
#         verbose_name = '用户'
#         verbose_name_plural = '用户'

class UserInfor(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.EmailField()


class Test(models.Model):
    name = models.CharField(max_length=20)


class Status(models.TextChoices):
    UNSTARTED = 'u', "Not started yet"
    ONGOING = 'o', "Ongoing"
    FINISHED = 'f', "Finished"


class Task(models.Model):
    name = models.CharField(verbose_name="Task name", max_length=65, unique=True)
    status = models.CharField(verbose_name="Task status", max_length=1, choices=Status.choices)

    class Meta:
        verbose_name = "任务"
        verbose_name_plural = "任务"

    def __str__(self):
        return self.name
