from django.db import models

class Article(models.Model):
    ar_name = models.CharField(max_length=100)
    ar_pic = models.TextField()
    ar_text = models.TextField()
    ar_date = models.DateTimeField()
    ar_com = models.IntegerField(default=0)

class Comments(models.Model):
    com_to = models.IntegerField()
    com_text = models.TextField(max_length=1000)
    com_name = models.CharField(max_length=20, default='No Name')