"""
UI tests for login and registration on Automation Exercise.
"""
import pytest
from src.pages.login_page import LoginPage


@pytest.mark.ui
class TestLogin:
    """End-to-end tests for user authentication."""

    def test_register_and_logout(self, page, api_client):
        """
        Register a new user via UI, verify logged-in state, then logout.
        Generates a unique user so the registration flow is exercised.
        """
        import uuid

        unique_id = str(uuid.uuid4())[:8]
        user = {
            "name": f"UI Test {unique_id}",
            "email": f"ui_{unique_id}@example.com",
            "password": "UiPass123!",
            "firstname": "UI",
            "lastname": "Test",
            "address1": "123 UI Street",
            "country": "United States",
            "state": "California",
            "city": "Los Angeles",
            "zipcode": "90001",
            "mobile_number": "+13105551234",
        }

        login_page = LoginPage(page)

        # Step 1: Navigate to login page
        login_page.goto_login()
        login_page.assert_login_page_visible()

        # Step 2: Fill signup form
        login_page.signup(user["name"], user["email"])

        # Step 3: Fill account details (registration form)
        from src.pages.registration_page import RegistrationPage
        reg_page = RegistrationPage(page)
        reg_page.fill_account_details(
            password=user["password"],
            firstname=user["firstname"],
            lastname=user["lastname"],
            address=user["address1"],
            country=user["country"],
            state=user["state"],
            city=user["city"],
            zipcode=user["zipcode"],
            mobile=user["mobile_number"],
        )
        reg_page.submit()

        # Step 4: Verify logged in
        login_page.assert_logged_in_as(user["name"])

        # Step 5: Logout
        login_page.logout()
        login_page.assert_login_page_visible()

        # Cleanup: remove the UI-created account
        try:
            api_client.delete_account(user["email"], user["password"])
        except Exception:
            pass

    def test_login_with_existing_user(self, page, test_user):
        """Login with an API-created user and verify account page access."""
        login_page = LoginPage(page)
        login_page.goto_login()
        login_page.login(test_user["email"], test_user["password"])
        login_page.assert_logged_in_as(test_user["name"])

    def test_register_with_existing_email(self, page, test_user):
        """Signup with an already registered email should show an error."""
        login_page = LoginPage(page)
        login_page.goto_login()
        login_page.signup(test_user["name"], test_user["email"])
        login_page.assert_existing_email_error()

    def test_login_with_invalid_credentials(self, page):
        """Login with invalid credentials should show an error."""
        login_page = LoginPage(page)
        login_page.goto_login()
        login_page.login("invalid_user@example.com", "wrongpassword")
        login_page.assert_invalid_login_error()
