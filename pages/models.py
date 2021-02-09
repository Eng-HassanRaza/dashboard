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