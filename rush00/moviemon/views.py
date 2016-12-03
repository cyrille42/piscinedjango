from django.shortcuts import render
from django.conf import settings
import requests
import json
# Gere les battles et le moviedex

def test(request):
	string = requests.get('http://www.omdbapi.com/?t=frozen&y=&plot=short&r=json')
	parse = json.loads(string.text)
	# for i in settings.ID_MMON:
	# 	string += requests.get('http://www.omdbapi.com/?t='+i+'&y=&plot=short&r=json')
	return render(request, 'moviemon/test.html', {'test' : string.json()})