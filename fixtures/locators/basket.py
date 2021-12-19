from selenium.webdriver.common.by import By


class BasketLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "i.material-icons")
    BASKET_TITLE = (By.CSS_SELECTOR, "li.collection-item")
    BUY_BUTTON = (By.CSS_SELECTOR, "button.btn")
