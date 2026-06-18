"""
Page object for the Product Details page.
URL: /product_details/<id>
"""
from src.pages.base_page import BasePage


class ProductDetailsPage(BasePage):
    """Encapsulates interactions on a product detail page."""

    _PRODUCT_NAME = ".product-information h2"
    _PRODUCT_PRICE = ".product-information span span"
    _AVAILABILITY = ".product-information p:has-text('Availability:')"
    _CONDITION = ".product-information p:has-text('Condition:')"
    _BRAND = ".product-information p:has-text('Brand:')"
    _QUANTITY = "#quantity"
    _ADD_TO_CART_BUTTON = "button.cart"

    def set_quantity(self, quantity: int) -> "ProductDetailsPage":
        self.fill(self._QUANTITY, str(quantity))
        return self

    def add_to_cart(self) -> "ProductDetailsPage":
        self.click(self._ADD_TO_CART_BUTTON)
        return self

    def assert_product_details_visible(self) -> "ProductDetailsPage":
        self.assert_element_visible(self._PRODUCT_NAME)
        self.assert_element_visible(self._PRODUCT_PRICE)
        self.assert_element_visible(self._AVAILABILITY)
        self.assert_element_visible(self._CONDITION)
        self.assert_element_visible(self._BRAND)
        return self

    def get_product_name(self) -> str:
        return self.get_text(self._PRODUCT_NAME)
