from django.db import models
from django.contrib.auth.models import User
import os

class MainCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/team_building/tag/{self.slug}'

class TeamMatchingPost(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    main_category = models.ForeignKey(MainCategory, null=True, blank=True, on_delete=models.SET_NULL)
    sub_category = models.ForeignKey(SubCategory, null=True, blank=True, on_delete=models.SET_NULL)

    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_comment_count(self):
        return self.comment_set.count()

    def get_absolute_url(self):
        return f'/team/{self.pk}/'


class Comment(models.Model):
    teammatchingpost = models.ForeignKey(TeamMatchingPost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}""{self.content}'

    def get_absolute_url(self):
        return f'{self.teammatchingpost.get_absolute_url()}#comment-{self.pk}'

