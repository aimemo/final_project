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

    def plus_quantity(self):
        self.custom_click_element(locator=BasketLocators.PRODUCT_PLUS)

    def minus_quantity(self):
        self.custom_click_element(locator=BasketLocators.PRODUCT_MINUS)

    def current_quantity(self):
        product_line = self.custom_get_text(locator=BasketLocators.BASKET_TITLE)
        added_product = product_line[1]
        current_quantity = added_product[(added_product.find("x") + 1): (added_product.find("add"))]
        return float(current_quantity)

    def delete_product(self):
        self.custom_click_element(locator=BasketLocators.PRODUCT_DELETE)

    def buy_products(self):
        self.custom_click_element(locator=BasketLocators.BUY_BUTTON_BASKET)
