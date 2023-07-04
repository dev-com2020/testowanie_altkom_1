import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def guru1():
    home_page = 'https://demo.guru99.com/test/newtours/register.php'
    driver = webdriver.Chrome()
    driver.get(home_page)
    wait = WebDriverWait(driver, 10)
    frame = wait.until(EC.presence_of_element_located((By.ID, "gdpr-consent-notice")))
    driver.switch_to.frame(frame)
    time.sleep(5)
    driver.find_element(By.ID, 'save').click()
    driver.switch_to.default_content()
    driver.find_element(By.NAME, 'firstName').send_keys('Selenium')
    driver.find_element(By.NAME, 'lastName').send_keys('Python')
    country = Select(driver.find_element(By.NAME, 'country'))
    country.select_by_value('INDIA')
    driver.find_element(By.ID, 'email').send_keys('')
    driver.find_element(By.NAME, 'password').send_keys('Python')

    time.sleep(10)


guru1()
