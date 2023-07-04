import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def guru1():
    home_page = 'https://output.jsbin.com/osebed/2'
    driver = webdriver.Chrome()
    driver.get(home_page)
    fruits = Select(driver.find_element(By.ID, 'fruits'))
    fruits.select_by_index(1)
    fruits.select_by_value("orange")

    time.sleep(10)


guru1()