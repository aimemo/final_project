"""
Tests for basket:
1. Increase quantity of product
2. Decrease quantity of product
3. Deleting product from basket
4. Buying of product
"""


class TestBasket:
    def test_increase_product(self, app):
        """
        Steps:
        1. Open start page
        2. Random choice of product
        3. Search of random product
        4. Add product to the basket
        5. Open the basket
        6. Check quantity of product
        7. Add item of product (increase quantity)
        8. Check quantity of product
        """
        app.open_start_page()
        item = app.search.random_item()
        app.search.search_item(data=item)
        app.basket.add_to_basket()
        app.basket.open_basket()
        product_quantity = app.basket.current_quantity()
        app.basket.plus_quantity()
        product_quantity_new = app.basket.current_quantity()
        assert product_quantity_new > product_quantity

    def test_decrease_product(self, app):
        """
        Steps:
        1. Open start page
        2. Random choice of product
        3. Search of random product
        4. Add product to the basket
        5. Open the basket
        6. Check quantity of product
        7. Remove item of product (decrease quantity)
        8. Check quantity of product
        """
        app.open_start_page()
        item = app.search.random_item()
        app.search.search_item(data=item)
        app.basket.add_to_basket()
        app.basket.open_basket()
        product_quantity = app.basket.current_quantity()
        app.basket.minus_quantity()
        product_quantity_new = app.basket.current_quantity()
        assert product_quantity_new < product_quantity

    def test_delete_product(self, app):
        """
        Steps:
        1. Open start page
        2. Random choice of product
        3. Search of random product
        4. Add product to the basket
        5. Open the basket
        6. Delete product from basket
        7. Check product delete from basket
        """
        app.open_start_page()
        item = app.search.random_item()
        app.search.search_item(data=item)
        app.basket.add_to_basket()
        app.basket.open_basket()
        app.basket.current_quantity()
        basket_text = app.basket.basket_text()
        basket_product = basket_text[1]
        assert item in basket_product
        app.basket.delete_product()
        assert item not in basket_text

    def test_buy_product(self, app):
        """
        Steps:
        1. Open start page
        2. Random choice of product
        3. Search of random product
        4. Add product to the basket
        5. Open the basket
        6. Check quantity of product
        7. Add item of product (increase quantity)
        8. Buy products
        8. Check basket is empty
        """
        app.open_start_page()
        item = app.search.random_item()
        app.search.search_item(data=item)
        app.basket.add_to_basket()
        app.basket.open_basket()
        product_quantity = app.basket.current_quantity()
        app.basket.plus_quantity()
        product_quantity_new = app.basket.current_quantity()
        assert product_quantity_new > product_quantity
        app.basket.buy_products()
        basket_text = app.basket.basket_text()
        basket_product = basket_text[1]
        assert "Cart is Empty" in basket_product
