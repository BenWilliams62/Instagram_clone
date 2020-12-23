from django.contrib import admin
from .models import Post, Likes, Follows, Comments, Profile

# Register your models here.

admin.site.register(Post)
admin.site.register(Follows)
admin.site.register(Comments)
admin.site.register(Likes)
admin.site.register(Profile)