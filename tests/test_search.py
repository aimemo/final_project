"""
Tests for start page:
1. Search item with valid data
2. Search item with invalid data
3. Add item to the basket
"""


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
        2. Add item to the basket
        3. Open the basket
        4. Check item in the basket
        """
        pass

