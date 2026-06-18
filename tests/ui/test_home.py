"""
UI tests for the Automation Exercise home page and navigation.
"""
import uuid

import pytest

from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage
from src.pages.products_page import ProductsPage
from src.pages.contact_us_page import ContactUsPage


@pytest.mark.ui
class TestHomePage:
    """End-to-end tests for home page loading, navigation, and subscription."""

    def test_home_page_loads_successfully(self, page):
        """Home page should display logo and navigation."""
        home_page = HomePage(page)
        home_page.goto_home()
        home_page.assert_home_page_visible()

    def test_navigate_to_products_page(self, page):
        """Clicking Products link should navigate to products page."""
        home_page = HomePage(page)
        home_page.goto_home()
        home_page.click_products()
        ProductsPage(page).assert_product_visible("Blue Top")

    def test_navigate_to_signup_login_page(self, page):
        """Clicking Signup / Login link should navigate to login page."""
        home_page = HomePage(page)
        home_page.goto_home()
        home_page.click_signup_login()
        LoginPage(page).assert_login_page_visible()

    def test_navigate_to_contact_us_page(self, page):
        """Clicking Contact us link should navigate to contact page."""
        home_page = HomePage(page)
        home_page.goto_home()
        home_page.click_contact_us()
        ContactUsPage(page).assert_contact_page_visible()

    def test_subscribe_to_newsletter(self, page):
        """Subscribing with a valid email should show success message."""
        unique_email = f"sub_{uuid.uuid4().hex[:8]}@example.com"
        home_page = HomePage(page)
        home_page.goto_home()
        home_page.subscribe(unique_email)
        home_page.assert_subscription_success()
