from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from pages.models import Pricing_Page
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
    is_bookmark = models.BooleanField(default=False)
    body = models.TextField()
    image = models.ImageField(upload_to = 'insights/', default = 'insights/img01.jpg')
    tags = TaggableManager()

    def __str__(self):
        return "%s (%s)" % (self.title, self.author.first_name)

class Slider(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'insights/', default = 'insights/img01.jpg')
    button_url = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % (self.title)

class Success_Stories(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='insights/', default='insights/img01.jpg')
    detail = models.TextField()

    def __str__(self):
        return "%s" % (self.title)

class Pricing_Packages(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    saving = models.FloatField(default=0)
    monthly_price = models.FloatField(default=0)
    pricing_page = models.ForeignKey(Pricing_Page, on_delete=models.CASCADE, null=True, blank=True)
    # benefits = TaggableManager()

    def __str__(self):
        return "%s" % (self.title)

class Pricing_Features(models.Model):
    feature_name = models.CharField(max_length=255)
    pricing_page = models.ForeignKey(Pricing_Page, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return "%s" % (self.feature_name)

class Pricing_Features_Value(models.Model):
    feature_value = models.CharField(max_length=255)
    recommended = models.BooleanField(default=False)
    pricing_features = models.ForeignKey(Pricing_Features, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "%s" % (self.feature_value)

class Pricing(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    benefits = TaggableManager()
    pricing_features = models.ForeignKey(Pricing_Features,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return "%s" % (self.title)


class Team(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    role = models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(upload_to='insights/', default='insights/img01.jpg')
    detail = models.TextField()
    facebook = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return "%s" % (self.name)