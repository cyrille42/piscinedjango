from django.shortcuts import render, redirect
from django.conf import settings
import random
from .forms import RegisterForm, LoginForm, TipForm
from .models import Tip
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from django.core.urlresolvers import reverse

# manque uste l'autorefresh des anonymus session


def index(request):
	tip = Tip.objects.order_by('date')
	if request.user.is_authenticated():
		if request.method == "POST":
			form = TipForm(request.POST)
			if form.is_valid():
				post = form.save(commit=False)
				post.auteur = request.user
				post.date = timezone.now()
				post.save()
		else:
			form = TipForm()
		return render(request, 'ex00/index.html', {'form': form, 'post' : tip})
	else:
		if 'mycookie' in request.COOKIES:
			return render(request, 'ex00/index.html', {'post' : tip})
		number = random.randint(0, 9)
		cookie = settings.RANDOM_NAME[number]
		# cree dans dictionaire cookie notre valeur
		request.COOKIES['mycookie'] = cookie
		response = render(request, 'ex00/index.html', {'post' : tip})
		response.set_cookie('mycookie', cookie , max_age=42)
		return response

def register(request):
	if request.user.is_authenticated():
		return redirect('http://127.0.0.1:8000/')
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			if form.cleaned_data['confirm_password'] == form.cleaned_data['password']:
				User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
				user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
				if user is not None:#and user.is_active:
					auth.login(request, user)
				return redirect('http://127.0.0.1:8000/')
			else:
			 	form._errors['password'] = ['this isn\'t the same password']
	else:
		form = RegisterForm()
	return render(request, 'ex00/register.html', {'form': form}) 

def login(request):
	if request.user.is_authenticated():
		return redirect('http://127.0.0.1:8000/')
	if request.method == "POST":
		form = LoginForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:#and user.is_active:
			auth.login(request, user)
			return redirect('http://127.0.0.1:8000/')
		# else:
		# 	form._errors['username'] = ['Password/username didn\'t match']
	else:
		form = LoginForm()
	return render(request, 'ex00/login.html', {'form': form})

def logout(request):
	auth.logout(request)
	return redirect('http://127.0.0.1:8000/')