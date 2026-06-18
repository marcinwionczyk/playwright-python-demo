"""
Page object for the Products listing page.
URL: /products
"""
from playwright.sync_api import expect

from src.pages.base_page import BasePage


class ProductsPage(BasePage):
    """Encapsulates interactions on the products listing page."""

    _SEARCH_INPUT = "#search_product"
    _SEARCH_BUTTON = "#submit_search"
    _PRODUCT_ITEMS = ".features_items .product-image-wrapper"
    _PRODUCT_NAME = ".productinfo p"
    _VIEW_PRODUCT_LINK = "a[href^='/product_details/']"
    _ADD_TO_CART_OVERLAY = ".overlay-content a.add-to-cart"
    _CATEGORY_LINKS = "#accordian .panel-title a"
    _BRAND_LINKS = ".brands-name a"

    def goto_products(self) -> "ProductsPage":
        self.goto("/products")
        self.wait_for_load("domcontentloaded")
        return self

    def search_product(self, name: str) -> "ProductsPage":
        self.fill(self._SEARCH_INPUT, name)
        self.click(self._SEARCH_BUTTON)
        return self

    def select_category(self, category: str) -> "ProductsPage":
        """Select a category by visible text."""
        self.page.get_by_role("link", name=category).click()
        return self

    def select_brand(self, brand: str) -> "ProductsPage":
        """Select a brand by visible text."""
        self.page.get_by_role("link", name=brand).click()
        return self

    def view_product(self, product_name: str) -> "ProductsPage":
        """Click view product for the matching product name."""
        item = self.page.locator(self._PRODUCT_ITEMS).filter(has_text=product_name)
        item.locator(self._VIEW_PRODUCT_LINK).click()
        return self

    def add_product_to_cart(self, product_name: str) -> "ProductsPage":
        """Hover over a product and click Add to cart."""
        item = self.page.locator(self._PRODUCT_ITEMS).filter(has_text=product_name)
        item.hover()
        item.locator(self._ADD_TO_CART_OVERLAY).click()
        return self

    def get_product_count(self) -> int:
        return self.find_all(self._PRODUCT_ITEMS).count()

    def assert_product_visible(self, product_name: str) -> "ProductsPage":
        locator = self.page.locator(self._PRODUCT_ITEMS).filter(has_text=product_name)
        expect(locator).to_be_visible()
        return self

    def assert_no_products_found(self) -> "ProductsPage":
        """Assert products list is empty after a search with no results."""
        self.assert_text_visible("Searched Products")
        assert self.get_product_count() == 0, "Expected no products in search results"
        return self
