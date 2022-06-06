from django.contrib.auth.models import User


def create_user_in_database(email, password):
    user = User.objects.create_user(email.split()[0], email, password)
    user.save()
