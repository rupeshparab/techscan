from __future__ import unicode_literals

from django.db import models  # noqa


# Create your models here.
class Technology(models.Model):
        name = models.CharField(max_length=100, unique=True)
        image_url = models.CharField(max_length=200, default='https://www.shareicon.net/download/128x128/2016/11/14/851937_stack_512x512.png')
        repo_count = models.IntegerField(default=0)
        created_at = models.DateTimeField(auto_now=True)

        def __unicode__(self):
                return self.name

        def __str__(self):
            return '%s - %s' % (self.name, self.repo_count)

class Author(models.Model):
        name = models.CharField(max_length=100)
        username = models.CharField(max_length=100, unique=True)
        avatar = models.CharField(max_length=200, default='https://www.shareicon.net/download/128x128/2016/11/14/851937_stack_512x512.png')
        desc = models.CharField(max_length=400, blank=True)
        stars = models.IntegerField(default=0)
        followers = models.IntegerField(default=0)
        following = models.IntegerField(default=0)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __unicode__(self):
                return self.name

        def __str__(self):
            return self.name

class Repository(models.Model):
        name = models.CharField(max_length=100, unique=True)
        author = models.ForeignKey(Author, on_delete=models.CASCADE)
        url = models.CharField(max_length=200, default='https://www.github.com/')
        desc = models.CharField(max_length=400, blank=True)
        technology = models.CharField(max_length=400, blank=True)
        tags = models.CharField(max_length=400, blank=True)
        forks = models.IntegerField(default=0)
        stars = models.IntegerField(default=0)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __unicode__(self):
                return self.name

        def __str__(self):
            return self.name
