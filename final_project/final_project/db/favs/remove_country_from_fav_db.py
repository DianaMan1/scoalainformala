from final_project.models import FavCountry


def remove_country_from_fav_db(user_id, country_code):
    fav_country = FavCountry.objects.filter(user_id= user_id, country_code= country_code)

    for item in fav_country:
        item.delete()
