"""
Top-level structure Application for access to another pages
"""
from fixtures.pages.basket import Basket
from fixtures.pages.search import Search


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.search = Search(self)
        self.basket = Basket(self)

    # Opening the start page
    def open_start_page(self):
        self.driver.get(self.url)

    # Closing the browser
    def quit(self):
        self.driver.quit()
