"""
Page object for the Shopping Cart page.
URL: /view_cart
"""
from playwright.sync_api import expect

from src.pages.base_page import BasePage


class CartPage(BasePage):
    """Encapsulates interactions on the cart page."""

    _CART_ROWS = "#cart_info_table tbody tr"
    _PRODUCT_NAME = ".cart_description h4 a"
    _PRODUCT_PRICE = ".cart_price p"
    _PRODUCT_QUANTITY = ".cart_quantity button"
    _PRODUCT_TOTAL = ".cart_total .cart_total_price"
    _REMOVE_BUTTON = ".cart_delete a.cart_quantity_delete"
    _PROCEED_TO_CHECKOUT_BUTTON = ".check_out"
    _EMPTY_CART_MESSAGE = "#empty_cart"
    _LOGIN_REGISTER_PROMPT = ".modal-body a[href='/login']"
    _CHECKOUT_MODAL = "#checkoutModal"

    def goto_cart(self) -> "CartPage":
        self.goto("/view_cart")
        self.wait_for_load()
        return self

    def proceed_to_checkout(self) -> "CartPage":
        self.click(self._PROCEED_TO_CHECKOUT_BUTTON)
        return self

    def remove_product(self, product_name: str) -> "CartPage":
        """Remove a product from the cart by name."""
        row = self.page.locator(self._CART_ROWS).filter(has_text=product_name)
        row.locator(self._REMOVE_BUTTON).click()
        return self

    def get_product_quantity(self, product_name: str) -> str:
        row = self.page.locator(self._CART_ROWS).filter(has_text=product_name)
        return row.locator(self._PRODUCT_QUANTITY).inner_text()

    def assert_product_in_cart(self, product_name: str) -> "CartPage":
        row = self.page.locator(self._CART_ROWS).filter(has_text=product_name)
        expect(row.locator(self._PRODUCT_NAME)).to_be_visible()
        return self

    def assert_product_not_in_cart(self, product_name: str) -> "CartPage":
        row = self.page.locator(self._CART_ROWS).filter(has_text=product_name)
        expect(row).to_have_count(0)
        return self

    def assert_login_or_register_prompt(self) -> "CartPage":
        self.assert_element_visible(self._CHECKOUT_MODAL)
        self.assert_element_visible(self._LOGIN_REGISTER_PROMPT)
        return self

    def assert_cart_empty(self) -> "CartPage":
        self.assert_element_visible(self._EMPTY_CART_MESSAGE)
        return self
