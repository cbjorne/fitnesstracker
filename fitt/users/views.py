from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import signup_form

def signup_view(request):
    if request.method == 'POST':
        form = signup_form(request.POST)


        if form.is_valid():
            form.save()

            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])

            login(request, user)
            return redirect('home')
    else:
        form = signup_form()
    
    return render(request, 'registration/signup.html', { 'form': form })