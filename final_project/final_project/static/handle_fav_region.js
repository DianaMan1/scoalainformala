var add_region_to_fav = (country_code, region_code) => {
    cookieStore.get("csrftoken").then((cookie) => {
        fetch('/add_region_to_fav', {
            headers: {
                'X-CSRFToken': cookie.value
            },
            method: 'POST',
            body: JSON.stringify({country_code, region_code})
        }).then((response) => response.json()).then((response) => {
            if(response.Status === 'Added') {
                icon = document.getElementById('icon-' + country_code + '-' + region_code + '--unfilled')

                if(!icon) return;

                icon.className += '-fill'
                icon.id = icon.id.replace('unfilled', 'filled')
            }
        })
    })
}

var remove_region_from_fav = (country_code, region_code) => {
    cookieStore.get("csrftoken").then((cookie) => {
        fetch('/remove_region_from_fav', {
            headers: {
                'X-CSRFToken': cookie.value
            },
            method: 'POST',
            body: JSON.stringify({country_code, region_code})
        }).then((response) => response.json()).then((response) => {
            if(response.Status === 'Removed') {
                icon = document.getElementById('icon-' + country_code + '-' + region_code + '--filled')

                if(!icon) return;

                icon.className = icon.className.replace('-fill', '')
                icon.id = icon.id.replace('filled', 'unfilled')
            }
        })
    })
}

var is_region_fav = (country_code, region_code) => {
    return cookieStore.get("csrftoken").then((cookie) => {
        return fetch('/is_region_fav', {
            headers: {
                'X-CSRFToken': cookie.value
            },
            method: 'POST',
            body: JSON.stringify({country_code, region_code})
        })
    })
}

var handle_fav_region = (country_code, region_code) => {
     if(!is_user_authenticated()) {
        response = window.confirm('You have to login to set your favorites.');
        if(response) {
            window.location.href = '/login';
        }

        return;
    }

    is_region_fav(country_code, region_code).then(response => response.json()).then((response) => {
        if(!response.fav) {
            add_region_to_fav(country_code, region_code)
        } else {
            remove_region_from_fav(country_code, region_code)
        }
    })
}