import requests
from final_project.api.pagination_helper import get_pagination, get_items_per_page, get_offset
from final_project.api.api_key import get_api_key

headers = {
    "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com",
    "X-RapidAPI-Key": get_api_key()
}


def decode_response(response):
    if response is None:
        return {
            "items": [],
            "current_page": None,
            "next_page": None,
            "previous_page": None,
            "total_pages": 0
        }

    decoded_response = response.json()
    pagination = get_pagination(decoded_response['metadata'])

    items = decoded_response['data']

    return_object = {
        'items': items
    }

    return_object.update(pagination)

    return return_object


def get_country_regions(country_id, page=1):
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/countries/" + country_id + '/regions'
    items_per_page = get_items_per_page()
    offset = get_offset(page)

    querystring = {"limit": items_per_page, "offset": offset, 'page': page}

    response = requests.request("GET", url, headers=headers, params=querystring)

    decoded_response = decode_response(response)

    return decoded_response
