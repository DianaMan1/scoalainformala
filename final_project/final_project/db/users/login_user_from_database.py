from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, HttpResponse


def login_user_from_database(request):
    email = request.POST['email']
    password = request.POST['password']

    username = User.objects.get(email=email.lower()).username

    user = authenticate(request, username=username, password=password)

    if user is not None:
        response = login(request, user)
        return HttpResponse(response)
