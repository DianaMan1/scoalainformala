from final_project.models import FavRegion


def add_region_to_fav_db(user_id, country_code, region_code):
    fav_region = FavRegion(user_id=user_id, country_code=country_code, iso_code=region_code)
    fav_region.save()

