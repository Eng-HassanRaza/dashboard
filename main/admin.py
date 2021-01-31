from django.contrib import admin
from .models import Post,Catagory,Slider

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'catagory')

admin.site.register(Catagory)
admin.site.register(Slider)
# Register your models here.
