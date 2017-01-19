from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
import random
from .models import Article, UserFavouriteArticle
from .forms import LoginForm, RegisterForm
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

def detail(request, pk):
	post = get_object_or_404(Article, pk=pk)
	return render(request, 'ex00/detail.html', {'post' : post})

def logout(request):
	auth.logout(request)
	return redirect('index:home')

def favorite(request):
	userid = request.user.id
	post = UserFavouriteArticle.objects.filter(user=userid)
	print(post)
	return render(request, 'ex00/favorite.html', {'post' : post})

def register(request):
	if request.user.is_authenticated():
		return redirect('index:home')
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			if form.cleaned_data['confirm_password'] == form.cleaned_data['password']:
				User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
				user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
				if user is not None:
					auth.login(request, user)
				return redirect('index:home')
			else:
			 	form._errors['password'] = ['this isn\'t the same password']
	else:
		form = RegisterForm()
	return render(request, 'ex00/register.html', {'form': form}) 