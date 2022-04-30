from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd
import csv
import matplotlib.pyplot as plt


base_url = 'https://www.mai.gov.ro/'
date_targetate = [20, 21, 22, 23, 24, 25, 26]
luna_targetata = 'ianuarie'


def exclude_first_element(list):
    del list[0]


def exclude_last_element(list):
    del list[-1]


def create_url_param(data, luna):
    return f'informare-covid-19-grupul-de-comunicare-strategica-{data}-{luna}-ora-13-00'


def create_url(data, luna):
    return f'{base_url}{create_url_param(data,luna)}'

browser = webdriver.Chrome(ChromeDriverManager().install())


def get_requests(data):
    url = create_url(data, luna_targetata)
    browser.get(url)
    table_rows = browser.find_elements(by=By.XPATH, value='//table[contains(.,"Număr de cazuri nou confirmate")]/tbody//tr')
    exclude_first_element(table_rows)
    exclude_last_element(table_rows)

    cazuri = []

    for row in table_rows:
        elements = row.find_elements(by=By.TAG_NAME, value='td')
        nume_judet = elements[1].text
        cazuri_noi = elements[3].text or '-'
        cazuri.append({nume_judet: cazuri_noi})

    return cazuri


def preia_cazuri():
    rezultat = []
    for data in date_targetate:
        istoric_cazuri = get_requests(data)
        rezultat.append({data: istoric_cazuri})

    return rezultat


def main():
     cazuri = preia_cazuri()
     df = pd.DataFrame(cazuri)
     df.to_csv("Covid.csv")


main()




