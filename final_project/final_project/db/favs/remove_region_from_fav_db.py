from final_project.models import FavRegion


def remove_region_from_fav_db(user_id, country_code, region_code):
    fav_regions = FavRegion.objects.filter(user_id=user_id, country_code=country_code, iso_code=region_code)

    for item in fav_regions:
        item.delete()
