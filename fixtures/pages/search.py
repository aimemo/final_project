import logging
import random

from fixtures.locators.basket import BasketLocators
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("moodle")


class Search(BasePage):
    """
    Methods of searching item
    1. Searching item
    2. Searching result
    3. Random choice product from current catalog
    """

    # Searching product in catalog
    def search_item(self, data):
        self.custom_input_element(locator=BasketLocators.SEARCH_INPUT, input=data)
        logger.info(f"Товар {data} введен в строку поиска")
        self.custom_click_element(locator=BasketLocators.SEARCH_BUTTON)
        logger.info(f"Запущен поиск товара")

    # Results of searching product
    def search_result(self):
        text = self.custom_get_text(locator=BasketLocators.CART_TITLE)
        return text

    # Choice random product from catalog
    def random_item(self):
        item = random.choice(self.custom_get_text(locator=BasketLocators.CART_TITLE))
        logger.info(f"Искомый товар выбран случайным образом. Это - {item}")
        return item
