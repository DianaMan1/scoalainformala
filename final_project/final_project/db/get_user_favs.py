from final_project.models import FavCountry


def get_user_favorites(user):
    user_favorites_list = list(FavCountry.objects.filter(user_id=user.id))
    user_favorites = []

    for item in user_favorites_list:
        user_favorites.append(item.country_code)

    return user_favorites
