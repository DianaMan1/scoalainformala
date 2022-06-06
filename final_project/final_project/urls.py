from django.urls import path
from . import views, user_views, views_for_favs
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('country/<country_code>/', views.country_detail_page, name='country_detail_page'),
    path('country/<country_code>/regions/', views.regions_page, name='regions_page'),
    path('country/<country_code>/cities/', views.cities_page, name='cities_page'),
    # path('admin/', admin.site.urls),
    path('login', user_views.login),
    path('logout', user_views.logout_user),
    path('sign_up', user_views.sign_up),
    path('create_user', user_views.create_user),
    path('login_user', user_views.login_user),
    path('edit_user', user_views.edit_user),
    path('edit_user_form_submit', user_views.edit_user_form_submit),
    path('add_country_to_fav', views_for_favs.add_country_to_fav),
    path('is_country_fav', views_for_favs.is_country_fav),
    path('remove_country_from_fav', views_for_favs.remove_country_from_fav),
    path('is_region_fav', views_for_favs.is_region_fav),
    path('add_region_to_fav', views_for_favs.add_region_to_fav),
    path('remove_region_from_fav', views_for_favs.remove_region_from_fav),
    path('is_city_fav', views_for_favs.is_city_fav),
    path('add_city_to_fav', views_for_favs.add_city_to_fav),
    path('remove_city_from_fav', views_for_favs.remove_city_from_fav)
]
