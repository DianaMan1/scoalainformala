var add_country_to_fav = (country_code) => {
    cookieStore.get("csrftoken").then((cookie) => {
        fetch('/add_country_to_fav', {
            headers: {
                'X-CSRFToken': cookie.value
            },
            method: 'POST',
            body: JSON.stringify(country_code)
        }).then((response) => response.json()).then((response) => {
            if(response.Status === 'Added') {
                icon = document.getElementById('icon-' + country_code + '--unfilled')

                if(!icon) return;

                icon.className += '-fill'
                icon.id = icon.id.replace('unfilled', 'filled')
            }
        })
    })
}

var remove_country_from_fav = (country_code) => {
    cookieStore.get("csrftoken").then((cookie) => {
        fetch('/remove_country_from_fav', {
            headers: {
                'X-CSRFToken': cookie.value
            },
            method: 'POST',
            body: JSON.stringify(country_code)
        }).then((response) => response.json()).then((response) => {
            if(response.Status === 'Removed') {
                icon = document.getElementById('icon-' + country_code + '--filled')

                if(!icon) return;

                icon.className = icon.className.replace('-fill', '')
                icon.id = icon.id.replace('filled', 'unfilled')
            }
        })
    })
}

var is_country_fav = (country_code) => {
    return cookieStore.get("csrftoken").then((cookie) => {
        return fetch('/is_country_fav', {
            headers: {
                'X-CSRFToken': cookie.value
            },
            method: 'POST',
            body: JSON.stringify(country_code)
        })
    })
}


var handle_fav = (country_code) => {
    if(!is_user_authenticated()) {
        response = window.confirm('You have to login to set your favorites.');
        if(response) {
            window.location.href = '/login';
        }

        return;
    }

    is_country_fav(country_code).then(response => response.json()).then((response) => {
        if(!response.fav) {
            add_country_to_fav(country_code)
        } else {
            remove_country_from_fav(country_code)
        }
    })
}
