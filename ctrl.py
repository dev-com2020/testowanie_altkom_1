import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
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
action = ActionChains(driver)
action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
time.sleep(5)
action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
time.sleep(5)
action.key_down(Keys.CONTROL).send_keys("x").key_up(Keys.CONTROL).perform()
time.sleep(5)
action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(5)



driver.quit()