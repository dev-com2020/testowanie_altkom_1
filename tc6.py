import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestGoogleSearch:

    @staticmethod
    def google_example_that_searches_for(search_string):
        driver = webdriver.Chrome()
        driver.get("https://google.com")
        try:
            element = driver.find_element(By.ID, "L2AGLb")
            element.click()
        except NoSuchElementException:
            pass
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(search_string)
        print(f"Searching for {search_string}")
        search_box.submit()
        WebDriverWait(driver, 10).until(EC.title_contains(search_string))
        print(f"Searching for {search_string}")
        driver.quit()

    def test_google_cheese_example(self):
        self.google_example_that_searches_for("cheese")

    def test_google_milk_example(self):
        self.google_example_that_searches_for("milk")

    def test_google_selenium_example(self):
        self.google_example_that_searches_for("selenium")

