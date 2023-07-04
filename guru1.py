import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def guru1():
    home_page = 'https://demo.guru99.com/test/radio.html'
    chrome_options = Options()
    chrome_options.add_argument("--disable-cookies")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(home_page)
    wait = WebDriverWait(driver, 10)
    frame = wait.until(EC.presence_of_element_located((By.ID, "gdpr-consent-notice")))
    driver.switch_to.frame(frame)
    time.sleep(5)
    driver.find_element(By.ID, 'save').click()
    driver.switch_to.default_content()
    radio1 = driver.find_element(By.ID, 'vfb-7-1')
    radio1.click()
    print('Radio button 1 is selected? ', radio1.is_selected())
    radio2 = driver.find_element(By.ID, 'vfb-7-2')
    radio2.click()
    print('Radio button 2 is selected? ', radio2.is_selected())
    option1 = driver.find_element(By.ID, 'vfb-6-0')
    option1.click()
    print('Option 1 is selected? ', option1.is_selected())
    option2 = driver.find_element(By.ID, 'vfb-6-1')
    option2.click()


    driver.quit()

guru1()
