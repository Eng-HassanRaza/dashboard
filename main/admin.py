from django.contrib import admin
from .models import Post,Catagory,Slider,Success_Stories,Pricing,Team

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'catagory')

admin.site.register(Catagory)
admin.site.register(Slider)
admin.site.register(Success_Stories)
# admin.site.register(Pricing)
admin.site.register(Team)
# Register your models here.
