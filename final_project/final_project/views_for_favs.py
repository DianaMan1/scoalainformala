from django.http import HttpResponseForbidden, JsonResponse
from json import loads
from django.contrib.auth.decorators import login_required

from .db.favs.add_city_to_fav_db import add_city_to_fav_db
from .db.favs.add_country_to_fav_db import add_country_to_fav_db
from .db.favs.add_region_to_fav_db import add_region_to_fav_db
from .db.favs.is_city_fav_db import is_city_fav_db
from .db.favs.is_country_fav_db import is_country_fav_db
from .db.favs.is_region_fav_db import is_region_fav_db
from .db.favs.remove_city_from_fav_db import remove_city_from_fav_db
from .db.favs.remove_country_from_fav_db import remove_country_from_fav_db
from .db.favs.remove_region_from_fav_db import remove_region_from_fav_db


@login_required
def add_country_to_fav(request):
    current_user = request.user

    if current_user is None:
        return HttpResponseForbidden()

    country_code = loads(request.body.decode('utf-8'))

    add_country_to_fav_db(current_user.id, country_code)

    response_data = {
        'Status': 'Added'
    }

    return JsonResponse(response_data)


@login_required
def remove_country_from_fav(request):
    current_user = request.user

    if current_user is None:
        return HttpResponseForbidden()

    country_code = loads(request.body.decode('utf-8'))

    remove_country_from_fav_db(current_user.id, country_code)

    response_data = {
        'Status': 'Removed'
    }

    return JsonResponse(response_data)


@login_required
def is_country_fav(request):
    current_user = request.user

    if current_user is None:
        return HttpResponseForbidden()

    country_code = loads(request.body.decode('utf-8'))
    response = is_country_fav_db(current_user.id, country_code)

    response_data = {
        'country_code': country_code,
        'fav': response
    }

    return JsonResponse(response_data)


@login_required
def is_region_fav(request):
    current_user = request.user

    if current_user is None:
        return HttpResponseForbidden()

    body = loads(request.body.decode('utf-8'))
    response = is_region_fav_db(current_user.id, body['country_code'], body['region_code'])

    response_data = {
        'fav': response
    }

    return JsonResponse(response_data)


@login_required
def add_region_to_fav(request):
    current_user = request.user

    if current_user is None:
        return HttpResponseForbidden()

    body = loads(request.body.decode('utf-8'))

    add_region_to_fav_db(current_user.id, body['country_code'], body['region_code'])

    response_data = {
        'Status': 'Added'
    }

    return JsonResponse(response_data)


@login_required
def remove_region_from_fav(request):
    current_user = request.user

    if current_user is None:
        return HttpResponseForbidden()

    body = loads(request.body.decode('utf-8'))

    remove_region_from_fav_db(current_user.id, body['country_code'], body['region_code'])

    response_data = {
        'Status': 'Removed'
    }

    return JsonResponse(response_data)


@login_required
def is_city_fav(request):
    current_user = request.user

    if current_user is None:
        return HttpResponseForbidden()

    body = loads(request.body.decode('utf-8'))
    response = is_city_fav_db(current_user.id, body['country_code'], body['city_id'])

    response_data = {
        'fav': response
    }

    return JsonResponse(response_data)


@login_required
def add_city_to_fav(request):
    current_user = request.user

    if current_user is None:
        return HttpResponseForbidden()

    body = loads(request.body.decode('utf-8'))

    add_city_to_fav_db(current_user.id, body['country_code'], body['city_id'])

    response_data = {
        'Status': 'Added'
    }

    return JsonResponse(response_data)


@login_required
def remove_city_from_fav(request):
    current_user = request.user

    if current_user is None:
        return HttpResponseForbidden()

    body = loads(request.body.decode('utf-8'))

    remove_city_from_fav_db(current_user.id, body['country_code'], body['city_id'])

    response_data = {
        'Status': 'Removed'
    }

    return JsonResponse(response_data)

