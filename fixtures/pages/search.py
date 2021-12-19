import logging
import random
import time

from selenium.webdriver.common.by import By

from fixtures.locators.basket import BasketLocators
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("moodle")


class Search(BasePage):
    """
    Methods of searching item
    1. Searching item
    2. Searching result
    3. Result has not found
    4.
    """
    def search_item(self, data):
        logger.info(f"Искомый товар - {data}")
        self.custom_input_element(locator=(By.ID, "email_inline"), input=data)
        self.custom_click_element(locator=(By.XPATH, "//button[text()='Search']"))

    def search_result(self):
        text = self.custom_get_text(locator=(By.CLASS_NAME, "card-title"))
        return text

    def random_item(self):
        item = random.choice(self.custom_get_text(locator=(By.CLASS_NAME, "card-title")))
        # logger.info(f"Выбран товар - {data}")
        return item






