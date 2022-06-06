var next_page = () => {
    query_string = window.location.search;

    params = new URLSearchParams(query_string);

    page = params.get('page') || 1

    page++

    params.delete('page')

    params.append('page', page)

    window.location.search = params
}

var previous_page = () => {
    query_string = window.location.search;

    params = new URLSearchParams(query_string);

    page = params.get('page') || 1

    page--

    if(page == 0) {
        return;
    }

    params.delete('page')

    params.append('page', page)

    window.location.search = params
}