from django.db import models
# from main.models import Pricing
# Create your models here.
class Pricing_Page(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    sub_title = models.CharField(max_length=255,null=True,blank=True)
    page_path = models.CharField(max_length=255,null=True,blank=True)
    # pricing = models.ForeignKey(Pricing)
    def __str__(self):
        return "%s" % (self.title)

class Impacx_Page(models.Model):
    box_title = models.CharField(max_length=255,null=True,blank=True)
    box_desc = models.CharField(max_length=255,null=True,blank=True)
    image = image = models.ImageField(upload_to='insights/', default='insights/img01.jpg')
    paragraph_title = models.CharField(max_length=255,null=True,blank=True)
    page_paragraph = models.TextField()
    def __str__(self):
        return "%s" % (self.box_title)

class Digitialization_Page(models.Model):
    box_title = models.CharField(max_length=255,null=True,blank=True)
    box_desc = models.CharField(max_length=255,null=True,blank=True)
    image = image = models.ImageField(upload_to='insights/', default='insights/img01.jpg')
    paragraph_title = models.CharField(max_length=255,null=True,blank=True)
    page_paragraph = models.TextField()
    def __str__(self):
        return "%s" % (self.box_title)