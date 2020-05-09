from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class Novel(models.Model):
  name = models.CharField(max_length=100)
  tags = models.CharField(max_length=20, null=True)
  description = models.CharField(max_length=300, null=True)
  imgSrc = models.CharField(max_length=200)
  author = models.CharField(max_length=10, null=True)
  updateTime = models.CharField(max_length=100, null=True)
  latestChapter = models.CharField(max_length=100, null=True)
  biqugePath = models.CharField(max_length=100, null=True)
  updateTimeOnServer = models.DateTimeField(default=timezone.now())

class Chapter(models.Model):
  novel_id = models.ForeignKey('Novel', on_delete=models.CASCADE)
  no = models.IntegerField()
  name = models.CharField(max_length=100)
  context_url = models.CharField(max_length=300)

class User(models.Model):
  name = models.CharField(max_length=20)
  passwd = models.CharField(max_length=60)


class History(models.Model):
  time = models.TimeField(default=timezone.now())
  book_name = models.CharField(max_length=100)
  user_id = models.IntegerField()
