"""
Tests for start page:
1. Search item with valid data
2. Search item with invalid data
3. Add item to the basket
"""
from fixtures.pages.constants import Constants


class TestSearch:
    def test_search_valid_data(self, app):
        """
        Steps:
        1. Open start page
        2. Input correct product name
        3. Search item
        4. Check result
        """
        app.open_start_page()
        item = "apples"
        app.search.search_item(data=item)
        result = app.search.search_result()
        assert item in result

    def test_search_invalid_data(self, app):
        """
        Steps:
        1. Open start page
        2. Input incorrect product name
        3. Search item
        4. Check result
        """
        app.open_start_page()
        item = "Чебурек"
        app.search.search_item(data=item)
        result = app.search.search_result()
        assert item not in result, 'Check not valid search'

    def test_add_item_to_basket(self, app):
        """
        Steps:
        1. Open start page
        2. Random choice of finding product
        3. Search of random product
        4. Add product to the basket
        5. Open the basket
        6. Check product in the basket
        """
        app.open_start_page()
        item = app.search.random_item()
        app.search.search_item(data=item)
        app.basket.add_to_basket()
        app.basket.open_basket()
        basket_text = app.basket.basket_text()
        basket_title = basket_text[0]
        assert basket_title == Constants.BASKET_TITLE
        basket_product = basket_text[1]
        assert item in basket_product


