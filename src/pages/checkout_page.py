"""
Page object for the Checkout and Payment pages.
URLs: /checkout, /payment
"""
from src.pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Encapsulates interactions on the checkout and payment pages."""

    # Checkout page
    _DELIVERY_ADDRESS = "#address_delivery"
    _BILLING_ADDRESS = "#address_invoice"
    _ORDER_SUMMARY = "#cart_info"
    _PLACE_ORDER_BUTTON = "a[href='/payment']"

    # Payment page
    _NAME_ON_CARD = '[data-qa="name-on-card"]'
    _CARD_NUMBER = '[data-qa="card-number"]'
    _CVC = '[data-qa="cvc"]'
    _EXPIRY_MONTH = '[data-qa="expiry-month"]'
    _EXPIRY_YEAR = '[data-qa="expiry-year"]'
    _PAY_BUTTON = '[data-qa="pay-button"]'
    _ORDER_SUCCESS_MESSAGE = "Order Placed!"
    _DOWNLOAD_INVOICE_BUTTON = "a:has-text('Download Invoice')"
    _CONTINUE_BUTTON = '[data-qa="continue-button"]'

    def goto_checkout(self) -> "CheckoutPage":
        self.goto("/checkout")
        self.wait_for_load()
        return self

    def place_order(self) -> "CheckoutPage":
        self.click(self._PLACE_ORDER_BUTTON)
        return self

    def fill_payment_details(
        self,
        name_on_card: str,
        card_number: str,
        cvc: str,
        expiry_month: str,
        expiry_year: str,
    ) -> "CheckoutPage":
        self.fill(self._NAME_ON_CARD, name_on_card)
        self.fill(self._CARD_NUMBER, card_number)
        self.fill(self._CVC, cvc)
        self.fill(self._EXPIRY_MONTH, expiry_month)
        self.fill(self._EXPIRY_YEAR, expiry_year)
        return self

    def pay_and_confirm_order(self) -> "CheckoutPage":
        self.click(self._PAY_BUTTON)
        return self

    def download_invoice(self) -> "CheckoutPage":
        self.click(self._DOWNLOAD_INVOICE_BUTTON)
        return self

    def assert_checkout_page_visible(self) -> "CheckoutPage":
        self.assert_element_visible(self._DELIVERY_ADDRESS)
        self.assert_element_visible(self._BILLING_ADDRESS)
        self.assert_element_visible(self._ORDER_SUMMARY)
        return self

    def assert_order_placed(self) -> "CheckoutPage":
        self.assert_text_visible(self._ORDER_SUCCESS_MESSAGE)
        return self
