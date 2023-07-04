import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


class AdditionalConditions:
    @staticmethod
    def jQueryAJAXCallsHaveCompleted():
        return lambda driver: driver.execute_script('return (window.jQuery != null) && (jQuery.active === 0);')


class AdditionalConditions_Angular:
    @staticmethod
    def angularHasFinishedProcessing():
        return driver.execute_script('return (window.angular != undefined) && '
                                     '(angular.element(document).injector() != undefined) && '
                                     '(angular.element(document).injector().get("$http").pendingRequests.length === 0)')

    def listener_is_registered_on_element(self, driver, listener_type, element):
        registered_listeners = driver.execute_script(
            "return (window.angular != undefined) && (angular.element(arguments[0]).data('$"
            "events') != undefined) && (angular.element(arguments[0]).data('$events')[arguments[1]] != undefined)",
            element, listener_type)

        if registered_listeners is not None:
            for listener in registered_listeners:
                if listener in listener_type:
                    return True
        return False

    def element_has_stopped_moving(self,driver,element: WebElement):
        init_location = element.location
        time.sleep(0.5)
        final_location = element.location
        return init_location == final_location


driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 10, 0.5)
# wait.until(AdditionalConditions.jQueryAJAXCallsHaveCompleted)
wait = WebDriverWait(driver, 15, poll_frequency=0.5,
                     ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
element = wait.until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
