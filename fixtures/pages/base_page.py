import time
import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as gitEC

logger = logging.getLogger("moodle")


class BasePage:
    def __init__(self, app):
        self.app = app

    # Find elements by given locator
    def custom_find_elements(self, locator, wait_time=3):
        try:
            elements = WebDriverWait(self.app.driver, wait_time).until(
                EC.presence_of_all_elements_located(locator),
                message=f"Can't find element by locator {locator}",
            )
        except:
            elements = []
        return elements

    # Input element to the search field
    def custom_input_element(self, locator, input, wait_time=2):
        element = self.custom_find_elements(locator, wait_time)[0]
        # time.sleep(2)
        element.send_keys(input)

    # Click element
    def custom_click_element(self, locator, wait_time=2):
        element = self.custom_find_elements(locator, wait_time)[0]
        # time.sleep(2)
        element.click()

    # Getting text from elements
    def custom_get_text(self, locator, wait_time=2):
        elements = self.custom_find_elements(locator, wait_time)
        # time.sleep(2)
        text = []
        try:
            for element in elements:
                text.append(element.text)
        except:
            text.append("product is not found")
        return text
