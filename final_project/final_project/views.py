from django.shortcuts import render, redirect
from .api.get_countries import get_countries
from .api.get_country_cities import get_country_cities
from .api.get_country_details import get_country_details
from .api.get_country_regions import get_country_regions
from .db.favs.is_city_fav_db import is_city_fav_db
from .db.favs.is_country_fav_db import is_country_fav_db
from .db.favs.is_region_fav_db import is_region_fav_db
from .db.get_user_favs import get_user_favorites

from time import sleep


def index(request):
    page = request.GET.get('page', 1)

    name_prefix = request.GET.get('name_prefix', '')

    user_favorites = get_user_favorites(request.user)

    data = get_countries(int(page), name_prefix)

    data.update({'favorites': user_favorites})

    return render(request, 'index.html', data)


def country_detail_page(request, *args, **kwargs):
    country_code = kwargs['country_code']

    data = get_country_details(country_code)
    is_fav = is_country_fav_db(request.user.id, country_code)
    data.update({'is_favorite': is_fav})

    return render(request, 'country_detail_page.html', data)


def regions_page(request, *args, **kwargs):
    page = request.GET.get('page', 1)
    country_code = kwargs['country_code']

    data = get_country_details(country_code)

    # GeoDB Api 1 request per second rule
    sleep(1.5)

    data.update({'is_favorite': is_country_fav_db(request.user.id, country_code)})

    regions = get_country_regions(country_code, int(page))

    for item in regions['items']:
        item['is_favorite'] = is_region_fav_db(request.user.id, country_code, item['isoCode'])

    data.update({'regions': regions})

    return render(request, 'regions_page.html', data)


def cities_page(request, *args, **kwargs):
    page = request.GET.get('page', 1)
    country_code = kwargs['country_code']
    data = get_country_details(country_code)

    # GeoDB Api 1 request per second rule
    sleep(1.5)

    data.update({'is_favorite': is_country_fav_db(request.user.id, country_code)})

    cities = get_country_cities(country_code, int(page))

    for item in cities['items']:
        item['is_favorite'] = is_city_fav_db(request.user.id, country_code, item['id'])

    data.update({'cities': cities})

    return render(request, 'cities_page.html', data)
