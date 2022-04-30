from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(ChromeDriverManager().install())
def browser_function():
    driver_path = "path/to/chromedriver"
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    chr_driver = webdriver.Chrome(driver_path, options=chr_options)
    chr_driver.get("https://target_website.com")

browser.get('https://www.emag.ro/#opensearch')
get_element = browser.find_element(by=By.ID, value='searchboxTrigger')
get_element.send_keys('telefon')
get_element.submit()

search_element = browser.find_element(by=By.ID, value='card_grid')
print(search_element.text)
