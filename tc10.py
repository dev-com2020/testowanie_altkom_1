from selenium import webdriver

driver = webdriver.Firefox()  # lub inna przeglądarka jak Chrome, Safari itp.
driver.set_page_load_timeout(15)  # ustawienie limitu czasu na 15 sekund
driver.get("https://www.google.com")  # otwarcie strony

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

DEFAULT_TIMEOUT_IN_SECONDS = 10

def reliable_find_element(driver, selector):
    try:
        element = WebDriverWait(driver, DEFAULT_TIMEOUT_IN_SECONDS).until(
            EC.presence_of_element_located((By.XPATH, selector))
        )
        return element
    except NoSuchElementException:
        print("Could not find {}".format(selector))
        return None

driver = webdriver.Chrome()
reliable_find_element(driver, "xpath_of_element")
wait = WebDriverWait(driver, 10, 0.5)
wait.until_not(EC.presence_of_element_located((By.ID, "loading_image")))
