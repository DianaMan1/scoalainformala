from final_project.models import FavRegion


def is_region_fav_db(user_id, country_code, region_code):
    fav_region = FavRegion.objects.filter(user_id=user_id, country_code=country_code, iso_code=region_code)

    if len(list(fav_region)) > 0:
        return True
    return False

