from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
#from login.models importUser

# Create your views here.
@login_required
def main_page(request):
	return render(request, 'login.html')

def signout(request):
	logout(request)
	return HttpResponseRedirect('/test/sign_in/')
	
def signin(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/test/main_page/')
		else:
			return HttpResponseRedirect('/test/sign_in/')
	return render(request, "signin.html")

def hello(request):
	return render(request, "hello.html")
