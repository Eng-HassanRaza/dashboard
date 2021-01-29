from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.

class Catagory(models.Model):
    name = models.CharField(max_length=64,null=True,blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.name)

class Post(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE,default=1)
    body = models.TextField()
    image = models.ImageField(upload_to = 'insights/', default = 'insights/img01.jpg')
    tags = TaggableManager()

    def __str__(self):
        return "%s (%s)" % (self.title, self.author.first_name)