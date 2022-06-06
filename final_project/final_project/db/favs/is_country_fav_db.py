from final_project.models import FavCountry


def is_country_fav_db(user_id, country_code):
    fav_country = FavCountry.objects.filter(user_id=user_id, country_code=country_code)

    if len(list(fav_country)) > 0:
        return True
    return False

