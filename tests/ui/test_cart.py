"""
UI tests for cart, checkout, and order placement.
"""
import pytest

from src.pages.home_page import HomePage
from src.pages.products_page import ProductsPage
from src.pages.product_details_page import ProductDetailsPage
from src.pages.cart_page import CartPage
from src.pages.cart_modal import CartModal
from src.pages.checkout_page import CheckoutPage
from src.pages.login_page import LoginPage


@pytest.mark.ui
class TestCart:
    """End-to-end tests for cart and checkout flows."""

    def test_add_product_to_cart_from_product_details(self, page):
        """Set quantity on product details and add to cart."""
        products_page = ProductsPage(page)
        products_page.goto_products()
        products_page.view_product("Blue Top")

        details_page = ProductDetailsPage(page)
        details_page.set_quantity(2)
        details_page.add_to_cart()
        CartModal(page).assert_modal_visible()

    def test_remove_product_from_cart(self, page):
        """Adding then removing a product should leave the cart empty."""
        products_page = ProductsPage(page)
        products_page.goto_products()
        products_page.add_product_to_cart("Blue Top")
        CartModal(page).click_view_cart()

        cart_page = CartPage(page)
        cart_page.remove_product("Blue Top")
        cart_page.assert_cart_empty()

    def test_checkout_prompts_login_for_guest(self, page):
        """Guest user clicking checkout should see login/register prompt."""
        products_page = ProductsPage(page)
        products_page.goto_products()
        products_page.add_product_to_cart("Blue Top")
        CartModal(page).click_view_cart()

        cart_page = CartPage(page)
        cart_page.proceed_to_checkout()
        cart_page.assert_login_or_register_prompt()

    def test_place_order_as_logged_in_user(self, page, test_user):
        """Logged-in user should be able to place an order."""
        # Login
        login_page = LoginPage(page)
        login_page.goto_login()
        login_page.login(test_user["email"], test_user["password"])
        login_page.assert_logged_in_as(test_user["name"])

        # Add product to cart
        home_page = HomePage(page)
        home_page.click_products()
        products_page = ProductsPage(page)
        products_page.add_product_to_cart("Blue Top")
        CartModal(page).click_view_cart()

        # Checkout
        cart_page = CartPage(page)
        cart_page.proceed_to_checkout()

        checkout_page = CheckoutPage(page)
        checkout_page.assert_checkout_page_visible()
        checkout_page.place_order()

        # Payment
        checkout_page.fill_payment_details(
            name_on_card=test_user["name"],
            card_number="4111111111111111",
            cvc="123",
            expiry_month="12",
            expiry_year="2030",
        )
        checkout_page.pay_and_confirm_order()
        checkout_page.assert_order_placed()

    def test_download_invoice_after_order(self, page, test_user):
        """After placing an order, invoice download button should be available."""
        # Login
        login_page = LoginPage(page)
        login_page.goto_login()
        login_page.login(test_user["email"], test_user["password"])
        login_page.assert_logged_in_as(test_user["name"])

        # Add product to cart
        home_page = HomePage(page)
        home_page.click_products()
        products_page = ProductsPage(page)
        products_page.add_product_to_cart("Blue Top")
        CartModal(page).click_view_cart()

        # Checkout and place order
        cart_page = CartPage(page)
        cart_page.proceed_to_checkout()

        checkout_page = CheckoutPage(page)
        checkout_page.place_order()
        checkout_page.fill_payment_details(
            name_on_card=test_user["name"],
            card_number="4111111111111111",
            cvc="123",
            expiry_month="12",
            expiry_year="2030",
        )
        checkout_page.pay_and_confirm_order()
        checkout_page.assert_order_placed()

        # Download invoice
        with page.expect_download() as download_info:
            checkout_page.download_invoice()
        download = download_info.value
        assert download.suggested_filename.endswith(".pdf") or "invoice" in download.suggested_filename.lower()
