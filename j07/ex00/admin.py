from django.contrib import admin
from .models import UserFavouriteArticle,Article
# Register your models here.

admin.site.register(UserFavouriteArticle)
admin.site.register(Article)