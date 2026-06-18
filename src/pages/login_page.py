"""
Page object for the Login / Signup page.
URL: /login
"""
from src.pages.base_page import BasePage


class LoginPage(BasePage):
    """Encapsulates interactions on the login and signup page."""

    # Selectors
    _SIGNUP_NAME = '[data-qa="signup-name"]'
    _SIGNUP_EMAIL = '[data-qa="signup-email"]'
    _SIGNUP_BUTTON = '[data-qa="signup-button"]'
    _LOGIN_EMAIL = '[data-qa="login-email"]'
    _LOGIN_PASSWORD = '[data-qa="login-password"]'
    _LOGIN_BUTTON = '[data-qa="login-button"]'
    _LOGOUT_LINK = 'a[href="/logout"]'
    _DELETE_ACCOUNT_LINK = 'a[href="/delete_account"]'
    _LOGGED_IN_TEXT = 'Logged in as'
    _EXISTING_EMAIL_ERROR = 'Email Address already exist!'
    _INVALID_LOGIN_ERROR = 'Your email or password is incorrect!'
    _ERROR_PARAGRAPH = "p[style*='color: red']"

    def goto_login(self) -> "LoginPage":
        self.goto("/login")
        self.wait_for_load()
        return self

    def signup(self, name: str, email: str) -> "LoginPage":
        self.fill(self._SIGNUP_NAME, name)
        self.fill(self._SIGNUP_EMAIL, email)
        self.click(self._SIGNUP_BUTTON)
        return self

    def login(self, email: str, password: str) -> "LoginPage":
        self.fill(self._LOGIN_EMAIL, email)
        self.fill(self._LOGIN_PASSWORD, password)
        self.click(self._LOGIN_BUTTON)
        return self

    def logout(self) -> "LoginPage":
        self.click(self._LOGOUT_LINK)
        return self

    def delete_account(self) -> "LoginPage":
        self.click(self._DELETE_ACCOUNT_LINK)
        return self

    def assert_login_page_visible(self) -> "LoginPage":
        self.assert_element_visible(self._SIGNUP_BUTTON)
        self.assert_element_visible(self._LOGIN_BUTTON)
        return self

    def assert_logged_in_as(self, name: str) -> "LoginPage":
        self.assert_text_visible(f"{self._LOGGED_IN_TEXT} {name}")
        return self

    def assert_existing_email_error(self) -> "LoginPage":
        self.assert_text_visible(self._EXISTING_EMAIL_ERROR)
        return self

    def assert_invalid_login_error(self) -> "LoginPage":
        self.assert_text_visible(self._INVALID_LOGIN_ERROR)
        return self
