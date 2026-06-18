"""
Page object for the API Testing page.
URL: /api_list
"""
from src.pages.base_page import BasePage


class APITestingPage(BasePage):
    """Encapsulates interactions on the API testing reference page."""

    _API_LIST_CONTAINER = ".row .col-sm-9"
    _API_ENDPOINT_HEADING = "h4.panel-title a"

    def goto_api_testing(self) -> "APITestingPage":
        self.goto("/api_list")
        self.wait_for_load()
        return self

    def get_api_endpoint_count(self) -> int:
        return self.find_all(self._API_ENDPOINT_HEADING).count()

    def assert_api_list_visible(self) -> "APITestingPage":
        self.assert_element_visible(self._API_LIST_CONTAINER)
        return self

    def assert_contains_methods(self) -> "APITestingPage":
        """Assert endpoint headings contain HTTP methods."""
        headings = self.find_all(self._API_ENDPOINT_HEADING)
        count = headings.count()
        assert count > 0, "No API endpoint headings found"
        texts = [headings.nth(i).inner_text() for i in range(count)]
        methods = {"GET", "POST", "PUT", "DELETE"}
        assert any(any(method in text for method in methods) for text in texts), \
            f"No HTTP method found in endpoint headings: {texts}"
        return self
