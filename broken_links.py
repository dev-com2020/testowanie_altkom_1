from selenium import webdriver
from selenium.webdriver.common.by import By
import requests


def broken_links():
    home_page = 'https://www.zlti.com'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(home_page)

    links = driver.find_elements(By.TAG_NAME, 'a')
    print('Total links on the page:', len(links))

    for link in links:
        url = link.get_attribute('href')
        print(url)

        if url is None or url == '':
            print('URL is either not configured for anchor tag or it is empty')
            continue

        if not url.startswith(home_page):
            print('URL belongs to another domain, skipping it.')
            continue

        try:
            response = requests.head(url)
            if response.status_code >= 400:
                print(url + ' is broken link')
            else:
                print(url + ' is valid link')
        except requests.exceptions.RequestException as e:
            print("Błąd:", e)

    driver.quit()


broken_links()