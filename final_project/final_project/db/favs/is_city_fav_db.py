from final_project.models import FavCity


def is_city_fav_db(user_id, country_code, city_id):
    fav_city = FavCity.objects.filter(user_id=user_id, country_code=country_code, city_id=city_id)

    if len(list(fav_city)) > 0:
        return True
    return False

