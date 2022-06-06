var prefix_input_callback = (event) => {
    query_string = window.location.search;

    params = new URLSearchParams(query_string);

    params.delete('name_prefix');
    params.delete('page');

    params.append('name_prefix', event.target.value)

    window.location.search = params
}
