from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .db.users.create_user_in_database import create_user_in_database
from .db.users.edit_user_in_database import edit_user_in_database
from .db.users.login_user_from_database import login_user_from_database
from django.contrib.auth import logout


def login(request):
    return render(request, 'users/login.html')


def sign_up(request):
    return render(request, 'users/sign_up.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def create_user(request):
    form_items = {}

    for key, value in request.POST.items():
        form_items[key] = value

    create_user_in_database(form_items['email'], form_items['password'])
    return redirect('/login')


def login_user(request):
    login_user_from_database(request)

    return redirect('/')


def edit_user(request):
    return render(request, 'users/edit_user.html')


@login_required
def edit_user_form_submit(request):
    form_items = {}

    current_user = request.user

    for key, value in request.POST.items():
        form_items[key] = value

    edit_user_in_database(current_user, form_items['username'], form_items['first_name'], form_items['last_name'])

    return redirect('/')
