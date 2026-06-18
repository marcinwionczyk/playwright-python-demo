"""
Shared modal helper for the Add-to-cart confirmation dialog.
"""
from src.pages.base_page import BasePage


class CartModal(BasePage):
    """Encapsulates the cart confirmation modal shown after adding a product."""

    _MODAL = "#cartModal"
    _CONTINUE_SHOPPING_BUTTON = "#cartModal .btn-success"
    _VIEW_CART_LINK = "#cartModal .modal-body a[href='/view_cart']"

    def click_continue_shopping(self) -> "CartModal":
        self.click(self._CONTINUE_SHOPPING_BUTTON)
        return self

    def click_view_cart(self) -> "CartModal":
        self.click(self._VIEW_CART_LINK)
        return self

    def assert_modal_visible(self) -> "CartModal":
        self.assert_text_visible("Added!")
        return self
