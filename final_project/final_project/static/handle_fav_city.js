var add_city_to_fav = (country_code, city_id) => {
    cookieStore.get("csrftoken").then((cookie) => {
        fetch('/add_city_to_fav', {
            headers: {
                'X-CSRFToken': cookie.value
            },
            method: 'POST',
            body: JSON.stringify({country_code, city_id})
        }).then((response) => response.json()).then((response) => {
            if(response.Status === 'Added') {
                icon = document.getElementById('icon-' + country_code + '-' + city_id + '--unfilled')

                if(!icon) return;

                icon.className += '-fill'
                icon.id = icon.id.replace('unfilled', 'filled')
            }
        })
    })
}

var remove_city_from_fav = (country_code, city_id) => {
    cookieStore.get("csrftoken").then((cookie) => {
        fetch('/remove_city_from_fav', {
            headers: {
                'X-CSRFToken': cookie.value
            },
            method: 'POST',
            body: JSON.stringify({country_code, city_id})
        }).then((response) => response.json()).then((response) => {
            if(response.Status === 'Removed') {
                icon = document.getElementById('icon-' + country_code + '-' + city_id + '--filled')

                if(!icon) return;

                icon.className = icon.className.replace('-fill', '')
                icon.id = icon.id.replace('filled', 'unfilled')
            }
        })
    })
}

var is_city_fav = (country_code, city_id) => {
    return cookieStore.get("csrftoken").then((cookie) => {
        return fetch('/is_city_fav', {
            headers: {
                'X-CSRFToken': cookie.value
            },
            method: 'POST',
            body: JSON.stringify({country_code, city_id})
        })
    })
}

var handle_fav_city = (country_code, city_id) => {
    if(!is_user_authenticated()) {
        response = window.confirm('You have to login to set your favorites.');
        if(response) {
            window.location.href = '/login';
        }

        return;
    }

    is_city_fav(country_code, city_id).then(response => response.json()).then((response) => {
        if(!response.fav) {
            add_city_to_fav(country_code, city_id)
        } else {
            remove_city_from_fav(country_code, city_id)
        }
    })
}