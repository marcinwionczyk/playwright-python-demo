"""
Base Page Object class for Playwright demo project.
Provides common interactions, waits, and assertions used across all page objects.
"""
from playwright.sync_api import Page, expect
from typing import Optional


class BasePage:
    """
    Abstract base for all page objects.
    Encapsulates common browser interactions and explicit waits.
    """

    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://automationexercise.com"

    def goto(self, path: str = "/") -> "BasePage":
        """Navigate to a path relative to base_url."""
        self.page.goto(f"{self.base_url}{path}")
        self.dismiss_cookie_consent()
        return self

    def wait_for_load(self, state: str = "networkidle") -> "BasePage":
        """Wait for page load state (load, domcontentloaded, networkidle)."""
        self.page.wait_for_load_state(state)
        return self

    def dismiss_cookie_consent(self) -> "BasePage":
        """Dismiss the cookie-consent banner/dialog if it appears."""
        consent_root = self.page.locator(".fc-consent-root")
        try:
            consent_root.wait_for(state="visible", timeout=3000)
        except Exception:
            return self

        for selector in [
            ".fc-cta-consent",
            ".fc-cta-do-not-consent",
            'button:has-text("Consent")',
            'button:has-text("Accept")',
            'button:has-text("Reject")',
            ".fc-button-label",
        ]:
            button = self.page.locator(selector).first
            if button.is_visible(timeout=1000):
                button.click()
                break

        consent_root.wait_for(state="hidden", timeout=5000)
        return self

    def find(self, selector: str, timeout: Optional[int] = None):
        """Find a single element with explicit wait."""
        return self.page.locator(selector).first

    def find_all(self, selector: str):
        """Find all elements matching selector."""
        return self.page.locator(selector)

    def click(self, selector: str, force: bool = False) -> "BasePage":
        """Click element after ensuring it is visible and enabled."""
        element = self.find(selector)
        element.wait_for(state="visible", timeout=10000)
        element.click(force=force)
        return self

    def fill(self, selector: str, text: str) -> "BasePage":
        """Clear and fill an input field."""
        element = self.find(selector)
        element.wait_for(state="visible", timeout=10000)
        element.fill(text)
        return self

    def get_text(self, selector: str) -> str:
        """Get inner text of an element."""
        return self.find(selector).inner_text()

    def is_visible(self, selector: str, timeout: int = 5000) -> bool:
        """Check if element is visible with short timeout."""
        try:
            self.find(selector).wait_for(state="visible", timeout=timeout)
            return True
        except Exception:
            return False

    def is_enabled(self, selector: str) -> bool:
        """Check if element is enabled."""
        return self.find(selector).is_enabled()

    def scroll_to(self, selector: str) -> "BasePage":
        """Scroll element into view."""
        self.find(selector).scroll_into_view_if_needed()
        return self

    def select_option(self, selector: str, value: str) -> "BasePage":
        """Select dropdown option by value."""
        self.find(selector).select_option(value)
        return self

    def assert_url_contains(self, fragment: str) -> "BasePage":
        """Assert current URL contains fragment."""
        expect(self.page).to_have_url(lambda url: fragment in url)
        return self

    def assert_text_visible(self, text: str) -> "BasePage":
        """Assert text is visible somewhere on the page."""
        expect(self.page.get_by_text(text)).to_be_visible()
        return self

    def assert_element_visible(self, selector: str) -> "BasePage":
        """Assert element is visible."""
        expect(self.find(selector)).to_be_visible()
        return self

    def assert_element_count(self, selector: str, count: int) -> "BasePage":
        """Assert number of elements matching selector."""
        expect(self.find_all(selector)).to_have_count(count)
        return self

    def take_screenshot(self, name: str) -> str:
        """Take a screenshot and save to test-results/screenshots."""
        from pathlib import Path
        path = Path(f"test-results/screenshots/{name}.png")
        path.parent.mkdir(parents=True, exist_ok=True)
        self.page.screenshot(path=str(path), full_page=True)
        return str(path)

    def handle_dialog(self, accept: bool = True) -> "BasePage":
        """Accept or dismiss the next dialog (alert/confirm)."""
        def handler(dialog):
            if accept:
                dialog.accept()
            else:
                dialog.dismiss()
        self.page.on("dialog", handler)
        return self
