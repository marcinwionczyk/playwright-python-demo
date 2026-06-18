"""
UI tests for the API Testing reference page.
"""
import pytest

from src.pages.api_testing_page import APITestingPage


@pytest.mark.ui
class TestAPITestingPage:
    """End-to-end tests for the API list page."""

    def test_api_list_contains_expected_endpoints(self, page):
        """API Testing page should display endpoints with HTTP methods."""
        api_page = APITestingPage(page)
        api_page.goto_api_testing()
        api_page.assert_api_list_visible()
        api_page.assert_contains_methods()
        assert api_page.get_api_endpoint_count() > 0
