# Ustaw opcje dla przeglądarki Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

# Utwórz nową sesję Chrome
driver = webdriver.Chrome(options=options)

# Przejdź do strony
driver.get("https://rsps100.com/vote/760")

# Czekaj, aż iframe będzie dostępny, a następnie przełącz się na niego
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[starts-with(@name, 'a-') and starts-with(@src, 'https://www.google.com/recaptcha')]")))

# Czekaj, aż element będzie dostępny do kliknięcia, a następnie kliknij go
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-checkmark"))).click()