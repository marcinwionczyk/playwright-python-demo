"""
UI tests for the Contact Us form.
"""
import uuid

import pytest

from src.pages.contact_us_page import ContactUsPage


@pytest.mark.ui
class TestContactUs:
    """End-to-end tests for contact form submission."""

    def test_submit_contact_form_with_valid_data(self, page):
        """Filling all fields and submitting should show success message."""
        unique_id = uuid.uuid4().hex[:8]
        contact_page = ContactUsPage(page)
        contact_page.goto_contact_us()
        contact_page.fill_contact_form(
            name=f"Test User {unique_id}",
            email=f"contact_{unique_id}@example.com",
            subject="Test subject",
            message="This is a test message submitted by the automated test suite.",
        )
        contact_page.submit()
        contact_page.assert_submission_success()

    def test_submit_contact_form_with_empty_required_fields(self, page):
        """Submitting an empty form should keep user on the page or show validation."""
        contact_page = ContactUsPage(page)
        contact_page.goto_contact_us()
        contact_page.submit()
        # HTML5 validation may prevent navigation; ensure success alert is not shown.
        assert not contact_page.is_visible(contact_page._SUCCESS_ALERT, timeout=2000)
