from django.db import models


# Create your models here.
class Novel(models.Model):
  name = models.CharField(max_length=30)
  tags = models.CharField(max_length=20, null=True)
  description = models.CharField(max_length=300, null=True)
  imgSrc = models.CharField(max_length=200)
  author = models.CharField(max_length=10, null=True)


class Chapter(models.Model):
  novel_id = models.ForeignKey('Novel', on_delete=models.CASCADE)
  no = models.IntegerField()
  name = models.CharField(max_length=30)
  context_url = models.CharField(max_length=300)
