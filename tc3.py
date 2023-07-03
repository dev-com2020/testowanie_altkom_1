from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")

try:
    element = driver.find_element(By.ID, "L2AGLb")
    element.click()
except NoSuchElementException:
    pass

search_box.click()
search_box.send_keys("selenium")
search_box.send_keys(Keys.ENTER)
driver.find_element(By.CSS_SELECTOR, ".eKjLze .LC20lb").click()

assert 'Selenium' in driver.page_source

driver.quit()