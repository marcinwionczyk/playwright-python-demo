"""
Page object for the Automation Exercise home page.
URL: /
"""
from src.pages.base_page import BasePage


class HomePage(BasePage):
    """Encapsulates interactions on the home page."""

    # Navigation selectors
    _LOGO = 'img[alt="Website for automation practice"]'
    _HOME_LINK = 'a[href="/"]'
    _PRODUCTS_LINK = 'a[href="/products"]'
    _SIGNUP_LOGIN_LINK = 'a[href="/login"]'
    _CONTACT_US_LINK = 'a[href="/contact_us"]'
    _CART_LINK = 'a[href="/view_cart"]'

    # Subscription selectors
    _SUBSCRIPTION_EMAIL = "#susbscribe_email"
    _SUBSCRIBE_BUTTON = "#subscribe"
    _SUBSCRIBE_SUCCESS_TEXT = "You have been successfully subscribed!"

    def goto_home(self) -> "HomePage":
        self.goto("/")
        self.wait_for_load()
        return self

    def click_products(self) -> "HomePage":
        self.click(self._PRODUCTS_LINK)
        return self

    def click_signup_login(self) -> "HomePage":
        self.click(self._SIGNUP_LOGIN_LINK)
        return self

    def click_contact_us(self) -> "HomePage":
        self.click(self._CONTACT_US_LINK)
        return self

    def click_cart(self) -> "HomePage":
        self.click(self._CART_LINK)
        return self

    def subscribe(self, email: str) -> "HomePage":
        """Subscribe to newsletter with the given email."""
        self.scroll_to(self._SUBSCRIPTION_EMAIL)
        self.fill(self._SUBSCRIPTION_EMAIL, email)
        self.click(self._SUBSCRIBE_BUTTON)
        return self

    def assert_home_page_visible(self) -> "HomePage":
        self.assert_element_visible(self._LOGO)
        self.assert_element_visible(self._PRODUCTS_LINK)
        self.assert_element_visible(self._SIGNUP_LOGIN_LINK)
        self.assert_element_visible(self._CONTACT_US_LINK)
        return self

    def assert_subscription_success(self) -> "HomePage":
        self.assert_text_visible(self._SUBSCRIBE_SUCCESS_TEXT)
        return self
