from final_project.models import FavCity


def add_city_to_fav_db(user_id, country_code, city_id):
    fav_city = FavCity(user_id=user_id, country_code=country_code, city_id=city_id)
    fav_city.save()

