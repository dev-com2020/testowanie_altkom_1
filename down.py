import os

from selenium import webdriver
from selenium.webdriver.common.by import By

download_dir = r"D:\projekty\testowanie1\src"
os.chdir(download_dir)

options = webdriver.ChromeOptions()
prefs = {"download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True}

options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/search?q=google&oq=google&aqs=chrome..69i57j0i131i433i512l4j69i60l3.2293j0j4&sourceid=chrome&ie=UTF-8")


# upload
upload= driver.find_element(By.ID, 'fruits')
upload.send_keys("C:\\Users\\Krzysztof\\Desktop\\test.txt")