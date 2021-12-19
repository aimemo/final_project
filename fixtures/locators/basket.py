from selenium.webdriver.common.by import By


class BasketLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "i.material-icons")
    BASKET_TITLE = (By.CSS_SELECTOR, "li.collection-item")
    BUY_BUTTON = (By.CSS_SELECTOR, "button.btn")
    PRODUCT_PLUS = (By.XPATH, "/html/body/div/div/main/ui/li[2]/i[2]")
    PRODUCT_MINUS = (By.XPATH, "/html/body/div/div/main/ui/li[2]/i[1]")
    PRODUCT_DELETE = (By.XPATH, "/html/body/div/div/main/ui/li[2]/span/i")
    BUY_BUTTON_BASKET = (
        By.XPATH,
        ".//li/button[@class = 'btn red btn-small' and contains(text(),'Buy')]",
    )
    SEARCH_INPUT = (By.ID, "email_inline")
    SEARCH_BUTTON = (By.XPATH, "//button[text()='Search']")
    CART_TITLE = (By.CLASS_NAME, "card-title")
