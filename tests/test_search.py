"""
Here will be comments
Tests for start page:
1. Search item with valid data
2. Search item with invalid data
3. Adding item to the basket
"""


class TestSearch:
    def test_search_valid_data(self, app):
        """
        Steps:
        1. Open main page
        2. Input item name
        3. Search item
        4. Check result
        """
        app.open_start_page()
        item = "apples"
        app.search.search_item(data=item)
        result = app.search.search_result()
        assert item in result
