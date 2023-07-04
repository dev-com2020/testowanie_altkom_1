from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

BROWSERS = {
    'firefox': {
        'driver': webdriver.Firefox,
        'options': FirefoxOptions,
        'service': None,
    },
    'chrome': {
        'driver': webdriver.Chrome,
        'options': ChromeOptions,
        'service': Service,
    },
    'edge': {
        'driver': webdriver.Edge,
        'options': EdgeOptions,
        'service': EdgeService,
    },
    # Add more browsers here
}


def get_webdriver(browser_name, headless=False):
    browser = BROWSERS[browser_name]
    options = browser['options']()

    if headless:
        options.add_argument('--headless')

    if browser['service']:
        driver = browser['driver'](service=browser['service'](), options=options)
    else:
        driver = browser['driver'](options=options)

    return driver


get_webdriver('edge', headless=False)