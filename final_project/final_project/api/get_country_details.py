import requests

from final_project.api.api_key import get_api_key

headers = {
    "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com",
    "X-RapidAPI-Key": get_api_key()
}


def get_country_details(country_code):
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/countries/" + country_code

    response = requests.request("GET", url, headers=headers)

    decoded_response = response.json()

    return decoded_response
