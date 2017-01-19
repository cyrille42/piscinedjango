from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=64,null=False)
    author = models.ForeignKey('auth.User',null = False)
    created = models.DateField(null = False)
    sysnopsis = models.CharField(max_length=312,null=False)
    content = models.TextField()
    def __str__(self):
        return self.title

class UserFavouriteArticle(models.Model):
	user = models.ForeignKey(User, null=False)
	article = models.ForeignKey(Article, null=False)
	def __str__(self):
		return self.article.title