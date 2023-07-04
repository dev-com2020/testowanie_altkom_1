import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestGoogleSearch:

    @staticmethod
    def login_main_func(username: str, password: str):
        driver = webdriver.Chrome()
        driver.get("https://ui.cogmento.com/")

        login_form = driver.find_element(By.NAME, "email")
        login_form.send_keys(username)

        password_form = driver.find_element(By.NAME, "password")
        password_form.send_keys(password)

        time.sleep(1)
        login_button = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div/div[3]")
        login_button.click()

        try:
            WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "user-display"), "Tomasz DEVCOM"))
            alert = driver.switch_to.alert
            alert.dismiss()
            WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "/html/body/div/div/div/form/div/div[3]/div"),
                                                    "Something went wrong..."))
        except Exception as e:
            print("Error: {} ".format(e.args))
        else:
            print("no error!")
        finally:
            driver.quit()


    def test_login_correct(self):
        self.login_main_func("kwp@tlen.pl", "xE3BKaw8yUxZmSU")

    def test_login_incorrect(self):
        self.login_main_func("kwp@tlen.pl", "xE3BKafdSU")