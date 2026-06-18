"""
Page object for the Contact Us page.
URL: /contact_us
"""
from src.pages.base_page import BasePage


class ContactUsPage(BasePage):
    """Encapsulates interactions on the contact us page."""

    _NAME = '[data-qa="name"]'
    _EMAIL = '[data-qa="email"]'
    _SUBJECT = '[data-qa="subject"]'
    _MESSAGE = '[data-qa="message"]'
    _UPLOAD_FILE = "input[name='upload_file']"
    _SUBMIT_BUTTON = '[data-qa="submit-button"]'
    _SUCCESS_ALERT = ".status.alert.alert-success"

    def goto_contact_us(self) -> "ContactUsPage":
        self.goto("/contact_us")
        self.wait_for_load()
        return self

    def fill_contact_form(
        self,
        name: str,
        email: str,
        subject: str,
        message: str,
    ) -> "ContactUsPage":
        self.fill(self._NAME, name)
        self.fill(self._EMAIL, email)
        self.fill(self._SUBJECT, subject)
        self.fill(self._MESSAGE, message)
        return self

    def submit(self) -> "ContactUsPage":
        self.handle_dialog(accept=True)
        self.click(self._SUBMIT_BUTTON)
        return self

    def assert_contact_page_visible(self) -> "ContactUsPage":
        self.assert_element_visible(self._NAME)
        self.assert_element_visible(self._EMAIL)
        self.assert_element_visible(self._SUBJECT)
        self.assert_element_visible(self._MESSAGE)
        self.assert_element_visible(self._SUBMIT_BUTTON)
        return self

    def assert_submission_success(self) -> "ContactUsPage":
        self.assert_element_visible(self._SUCCESS_ALERT)
        return self
