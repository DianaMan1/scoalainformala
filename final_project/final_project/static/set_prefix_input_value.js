set_prefix_input_value = () => {
    query_string = window.location.search;

    params = new URLSearchParams(query_string);

    value = params.get('name_prefix')

    if(value) {
        document.querySelector('#prefix_input').setAttribute('value', value)
    }
};

set_prefix_input_value()