import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, app):
        self.app = app

    def custom_find_element(self, locator, wait_time=10):
        elements = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find element by locator {locator}")
        return elements

    def custom_input_element(self, locator, input, wait_time=10):
        element = self.custom_find_element(locator, wait_time)[0]
        time.sleep(2)
        element.send_keys(input)

    def custom_click_element(self, locator, wait_time=10):
        element = self.custom_find_element(locator, wait_time)[0]
        time.sleep(2)
        element.click()

    def custom_get_text(self, locator, wait_time=10):
        elements = self.custom_find_element(locator, wait_time)
        time.sleep(2)
        text = []
        for element in elements:
            text.append(element.text)
        return text
