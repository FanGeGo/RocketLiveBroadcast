from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from datetime import datetime
from django.contrib.auth.hashers import make_password


class MyUserManager(BaseUserManager):
    def create_user(self, account, nickname, is_student=True, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        # if not email:
        #    raise ValueError('Users must have an email address')
        user = self.model(account=account, nickname=nickname,
                          is_student=is_student)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, account, nickname, is_student, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            account=account, nickname=nickname, password=password, is_student=is_student)
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    account = models.CharField(max_length=250, unique=True)
    nickname = models.CharField(max_length=200)
    is_student = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'account'
    # 设置认证标识
    REQUIRED_FIELDS = ['nickname', 'is_student']

    def get_full_name(self):
        # The user is identified by their email address
        return self.account

    def get_short_name(self):
        # The user is identified by their email address
        return self.account

    def __str__(self):
        # __unicode__ on Python 2
        return self.account

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
    # Simplest possible answer: All admins are staff
        return self.is_admin
# Create your models here.


class LiveRoom(models.Model):
    room_name = models.CharField(max_length=100)
    room_introduction = models.TextField(null=True)
    room_img = models.ImageField(upload_to='img/covers', null=True)
    room_creator = models.ForeignKey(MyUser)
    created_time = models.DateTimeField(auto_now_add=True)
    active_mode = models.CharField(max_length=10, default='READY')


class Slide(models.Model):
    room_slide = models.FileField(upload_to='slide/orginal', null=False)
    converted_pdf = models.FileField(upload_to='slide/pdf', null=True)
    live_room = models.ForeignKey(LiveRoom)
    created_time = models.DateTimeField(auto_now_add=True)


class History(models.Model):
    room_id = models.IntegerField(primary_key=True)
    room_name = models.CharField(max_length=100)
    room_introduction = models.TextField(null=True)
    room_img = models.ImageField(upload_to='img/covers', null=False)
    room_creator = models.ForeignKey(MyUser)
    history_source = models.FileField(upload_to='video', null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    time_length = models.IntegerField(null=True)


class AllSilent(models.Model):
    room_id = models.IntegerField()
    is_allsilent = models.BooleanField()
    silent_time = models.DateTimeField()


class OneSilent(models.Model):
    room_id = models.IntegerField()
    user = models.CharField(max_length=100)
    is_silent = models.BooleanField()
    silent_time = models.DateTimeField()


class ChatHistory(models.Model):
    room_id = models.IntegerField()
    user = models.CharField(max_length=100)
    content = models.TextField()
    time = models.DateTimeField()


class VisitHistory(models.Model):
    room_id = models.IntegerField()
    user = models.CharField(max_length=100)
    visit_time = models.DateTimeField()
    leave_time = models.DateTimeField()
    is_refused = models.BooleanField()


class VertifyRegister(models.Model):
    account = models.CharField(max_length=100)
    vertifycode = models.CharField(max_length=100)
    vertifytime = models.DateTimeField(auto_now=True)

    def __str__(self):
        print(self.vertifytime)
        return "account:" + self.account + ", code:" + self.vertifycode
        # return "account:" + self.account + ", code:" + self.vertifycode + ", time:" + self.vertifytime.strftime("%Y-%m-%d %H:%M:%S")


class VertifyForgetpasswd(models.Model):
    account = models.CharField(max_length=100)
    vertifycode = models.CharField(max_length=100)
    vertifytime = models.DateTimeField(auto_now=True)
