from django.contrib import admin
from .models import Post
# from django.contrib.auth import User

class PostContribute(admin.ModelAdmin):
    list_display = ['title','author','created_date']
    search_fields = ('title',)
            
admin.site.register(Post,PostContribute)

