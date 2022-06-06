var is_user_authenticated = () => {
    searchedDiv = document.getElementById('user-is-authenticated');

    if(searchedDiv) {
        return true;
    }

    return false;
}