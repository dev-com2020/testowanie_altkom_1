from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

# driver.get("https://www.google.com")
#
# variable_data = 'Google'
#
# dynamic_xpath = "//*[text()='" + variable_data + "']"
# elements = driver.find_elements(By.XPATH, dynamic_xpath)
# print('liczba znalezionych elementów:', len(elements))

driver.get("https://www.google.com/search?q=google&oq=google&aqs=chrome..69i57j0i131i433i512l4j69i60l3.2293j0j4&sourceid=chrome&ie=UTF-8")
driver.set_window_size(1905, 1012)
element = driver.find_element(By.LINK_TEXT, "Google Maps")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, ".tF2Cxc > .yuRUbf .LC20lb")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, ".tF2Cxc > .yuRUbf .LC20lb").click()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element, 0, 0).perform()
driver.find_element(By.CSS_SELECTOR, "#L2AGLb > .QS5gu").click()
driver.find_element(By.ID, "APjFqb").click()
driver.find_element(By.ID, "APjFqb").send_keys("selenium")
driver.find_element(By.CSS_SELECTOR, ".eKjLze .LC20lb").click()
