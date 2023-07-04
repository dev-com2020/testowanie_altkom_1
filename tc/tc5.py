from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://ui.cogmento.com/")

inputBoxes = driver.find_elements(By.TAG_NAME, "input")

print('liczba elementów input', len(inputBoxes))

driver.quit()



