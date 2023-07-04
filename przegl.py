from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

def test_basic_service():
    service = ChromeService()
    service = FirefoxService()
    driver = webdriver.Chrome(service=service)

    driver.quit()


def test_driver_location(chromedriver_path):
    service = ChromeService(executable_path=chromedriver_path)

    driver = webdriver.Chrome(service=service)

    driver.quit()


def test_driver_port():
    service = ChromeService(port=1234)

    driver = webdriver.Chrome(service=service)

    driver.quit()


chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability("browserVersion", "67")
chrome_options.set_capability("platformName", "Windows XP")
driver = webdriver.Remote(
    command_executor='http://www.example.com',
    options=chrome_options
)
driver.get("http://www.google.com")
driver.quit()

# options = webdriver.IeOptions()
# options.attach_to_edge_chrome = True
# options.edge_executable_path = EDGE_BINARY
# driver = webdriver.Ie(options=options)

# /html/body/div[1]/div[1]/div[3]/main/div/div/section[1]/div/div[2]/div/section/div/div/form/div[1]/div/div/div/div/div/div[1]/input