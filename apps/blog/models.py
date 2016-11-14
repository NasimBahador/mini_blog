from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def login(self, data):
        response = {}
        user = User.userMgr.get(user_name = data['user_name'])
        if user:
            response['found'] = True
            response['id'] = user['id']
        else:
            response['found'] = False

class PostManager(models.Manager):
    def add(self, data):
        pass

class User(models.Model):
    user_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    content = models.CharField(max_length = 300)
    user = models.ForeignKey(User, related_name = 'user_post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    postMgr = PostManager()
