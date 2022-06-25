from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.db.models import Q

from .forms import LoginForm, RegisterForm
from .models import User
from ..store.models import Product


def home(request):
    product_spotlight = Product.objects.filter(Q(slug='glass-s') | Q(slug='hyperspectral-tv'))
    return render(request, 'core/home.html', {
        'product_spotlight': product_spotlight
    })

def _login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {
            'form': LoginForm()
        })
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            errors = []

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('core:home')
                else:
                    return redirect('core:home')
            else:
                errors.append('Incorrect username/password.')

                return render(request, 'accounts/login.html', {
                    'form': form,
                    'errors': errors
                })
        else:
            return render(request, 'accounts/login.html', {
                'form': form
            })

    else:
        return HttpResponse('Only GET and POST requests allowed.')

def _logout(request):
    logout(request)
    return redirect('core:home')

def register(request):
    if request.method == 'GET':
        return render(request, 'accounts/register.html', {
            'form': RegisterForm()
        })
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        errors = [] #TODO Put all the error-checking in the form and get it to render it straight away from that; remove all this code from here

        if len(form.data.get('username')) > 32:
            errors.append('The username is too long.')

        if len(form.data.get('username')) < 2:
            errors.append('The username is too short.')

        if form.data.get('password') != form.data.get('confirm_password'):
            errors.append('The passwords do not match.')

        if len(form.data.get('email')) > 127:
            errors.append('The email is too long.')

        if len(form.data.get('first_name')) > 127:
            errors.append('The first name is too long')

        if len(form.data.get('last_name')) > 127:
            errors.append('The last name is too long')

        if User.objects.filter(email=form.data.get('email')).exists():
            errors.append('A user with this email already exists.')

        if User.objects.filter(username=form.data.get('username')).exists():
            errors.append('A user with this username already exists.')

        if len(form.data.get('password')) < 6:
            errors.append('The password is too short.')

        if form.data.get('username') == '420' or form.data.get('username') == '69':
            errors.append('Nice')

        if errors:
            return render(request, 'accounts/register.html', {
                'form': RegisterForm(request.POST),
                'errors': errors
            })

        user = form.save(commit=False)
        user.password = make_password(form.data.get('password'))
        user.save()

        return redirect('core:home')
    else:
        return HttpResponse('Only GET and POST requests allowed.')
