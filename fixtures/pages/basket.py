import time
import logging

from fixtures.locators.basket import BasketLocators
from fixtures.pages.base_page import BasePage

logger = logging.getLogger("moodle")


class Basket(BasePage):
    def open_basket(self):
        self.custom_click_element(locator=BasketLocators.BASKET_BUTTON)
        logger.info(f"Открыта корзина")

    def add_to_basket(self):
        element = self.custom_find_elements(locator=BasketLocators.BUY_BUTTON)[1]
        time.sleep(2)
        element.click()
        logger.info(f"Товар добавлен в корзину")

    def basket_text(self):
        title = self.custom_get_text(locator=BasketLocators.BASKET_TITLE)
        return title

    def plus_quantity(self):
        self.custom_click_element(locator=BasketLocators.PRODUCT_PLUS)
        logger.info(f"Добавлена единица товара")

    def minus_quantity(self):
        self.custom_click_element(locator=BasketLocators.PRODUCT_MINUS)
        logger.info(f"Удалена единица товара")

    def current_quantity(self):
        product_line = self.custom_get_text(locator=BasketLocators.BASKET_TITLE)
        added_product = product_line[1]
        current_quantity = added_product[
            (added_product.find("x") + 1) : (added_product.find("add"))
        ]
        logger.info(f"Текущее количество единиц товара - {current_quantity}")
        return float(current_quantity)

    def delete_product(self):
        self.custom_click_element(locator=BasketLocators.PRODUCT_DELETE)
        logger.info(f"Товар удален из корзины")

    def buy_products(self):
        self.custom_click_element(locator=BasketLocators.BUY_BUTTON_BASKET)
        logger.info(f"Совершена покупка")
