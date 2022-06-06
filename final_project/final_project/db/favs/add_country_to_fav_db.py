from final_project.models import FavCountry


def add_country_to_fav_db(user_id, country_code):
    fav_country = FavCountry(user_id=user_id, country_code=country_code)
    fav_country.save()

