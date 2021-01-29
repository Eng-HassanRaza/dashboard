from django.contrib import admin
from .models import Post,Catagory

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'catagory')

admin.site.register(Catagory)
# Register your models here.
