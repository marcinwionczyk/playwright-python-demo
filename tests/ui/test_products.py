"""
UI tests for product listing, search, details, and filters.
"""
import pytest

from src.pages.home_page import HomePage
from src.pages.products_page import ProductsPage
from src.pages.product_details_page import ProductDetailsPage
from src.pages.cart_modal import CartModal


@pytest.mark.ui
class TestProducts:
    """End-to-end tests for product catalog functionality."""

    def test_search_for_non_existing_product(self, page):
        """Search with no matches should show 'No products found'."""
        products_page = ProductsPage(page)
        products_page.goto_products()
        products_page.search_product("nonexistentproduct12345")
        products_page.assert_no_products_found()

    def test_view_product_details(self, page):
        """Clicking view product should show product details page."""
        products_page = ProductsPage(page)
        products_page.goto_products()
        products_page.view_product("Blue Top")
        ProductDetailsPage(page).assert_product_details_visible()

    def test_filter_products_by_category(self, page):
        """Selecting a category should filter products."""
        products_page = ProductsPage(page)
        products_page.goto_products()
        products_page.select_category("Women")
        # After filtering by Women, at least one product should be displayed.
        assert products_page.get_product_count() > 0

    def test_filter_products_by_brand(self, page):
        """Selecting a brand should filter products."""
        products_page = ProductsPage(page)
        products_page.goto_products()
        products_page.select_brand("Polo")
        # After filtering by brand, at least one product should be displayed.
        assert products_page.get_product_count() > 0

    def test_add_product_to_cart_from_products_page(self, page):
        """Hover over product and add to cart should show confirmation modal."""
        products_page = ProductsPage(page)
        products_page.goto_products()
        products_page.add_product_to_cart("Blue Top")
        CartModal(page).assert_modal_visible()
