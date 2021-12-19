import time

from fixtures.locators.basket import BasketLocators
from fixtures.pages.base_page import BasePage


class Basket(BasePage):
    def open_basket(self):
        self.custom_click_element(locator=BasketLocators.BASKET_BUTTON)

    def add_to_basket(self):
        element = self.custom_find_element(locator=BasketLocators.BUY_BUTTON)[1]
        time.sleep(2)
        element.click()

    def basket_text(self):
        title = self.custom_get_text(locator=BasketLocators.BASKET_TITLE)
        return title
