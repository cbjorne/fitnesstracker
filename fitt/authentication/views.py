from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.contrib import messages

from .forms import LoginForm, SignupForm

def authenticate(request):
    return redirect('/login')

def signup(request):
    print(request.POST)
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
        else:
            print(request)
            print(form.errors.as_json())
            for error in form.errors.as_data()['__all__']:
                messages.error(request, error.message)
            return render(request, 'signup.html', { 'form': form })
    else:
        form = SignupForm()
        
    return render(request, 'signup.html', { 'form': form })

def login(request):
    print(request.POST)
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    
    else:
        form = LoginForm()
    
    return render(request, 'login.html', { 'form': form })