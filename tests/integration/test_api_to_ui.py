"""
Integration tests: API + UI cross-layer validation.
Proves system-level understanding by orchestrating backend and frontend.
"""
import pytest
from src.pages.login_page import LoginPage


@pytest.mark.integration
class TestAPItoUI:
    """Create data via API, interact via UI, verify consistency."""

    def test_api_created_user_can_login_via_ui(self, page, test_user):
        """
        1. User is created via API (test_user fixture)
        2. Login via UI
        3. Verify logged-in state
        4. Cleanup via API (fixture teardown)
        """
        login_page = LoginPage(page)
        login_page.goto_login()
        login_page.login(test_user["email"], test_user["password"])
        login_page.assert_logged_in_as(test_user["name"])

    def test_api_created_user_can_delete_account_via_ui(self, page, test_user):
        """
        1. Create user via API
        2. Login via UI
        3. Delete account via UI
        4. Verify redirected to home / login page
        """
        login_page = LoginPage(page)
        login_page.goto_login()
        login_page.login(test_user["email"], test_user["password"])
        login_page.assert_logged_in_as(test_user["name"])

        login_page.delete_account()
        login_page.assert_text_visible("Account Deleted!")
