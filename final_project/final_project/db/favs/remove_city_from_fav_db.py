from final_project.models import FavCity


def remove_city_from_fav_db(user_id, country_code, city_id):
    fav_cities = FavCity.objects.filter(user_id=user_id, country_code=country_code, city_id=city_id)

    for item in fav_cities:
        item.delete()
