from django.shortcuts import render, redirect
from django.conf import settings
import random
from .models import Article
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from django.core.urlresolvers import reverse


def home(request):
	return redirect(reverse('index:article'))

def login(request):
	if request.user.is_authenticated():
		return redirect('index:home')
	if request.method == "POST":
		form = LoginForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:#and user.is_active:
			auth.login(request, user)
			return redirect('index:home')
		# else:
		# 	form._errors['username'] = ['Password/username didn\'t match']
	else:
		form = LoginForm()
	return render(request, 'ex00/login.html', {'form': form})

def article(request):
	post = Article.objects.order_by('title')
	return render(request, 'ex00/article.html', {'post' : post})