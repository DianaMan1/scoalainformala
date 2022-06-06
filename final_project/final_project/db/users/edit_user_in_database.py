def edit_user_in_database(user, new_username, new_first_name, new_last_name):
    user.username = new_username
    user.first_name = new_first_name
    user.last_name = new_last_name
    user.save()
