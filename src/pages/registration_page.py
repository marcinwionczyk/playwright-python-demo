"""
Page object for the Account Registration page.
URL: /signup
"""
from src.pages.base_page import BasePage


class RegistrationPage(BasePage):
    """Encapsulates the signup / registration form."""

    # Selectors
    _MR_TITLE = "#id_gender1"
    _MRS_TITLE = "#id_gender2"
    _PASSWORD = '[data-qa="password"]'
    _DAY = '[data-qa="days"]'
    _MONTH = '[data-qa="months"]'
    _YEAR = '[data-qa="years"]'
    _FIRSTNAME = '[data-qa="first_name"]'
    _LASTNAME = '[data-qa="last_name"]'
    _ADDRESS = '[data-qa="address"]'
    _COUNTRY = '[data-qa="country"]'
    _STATE = '[data-qa="state"]'
    _CITY = '[data-qa="city"]'
    _ZIPCODE = '[data-qa="zipcode"]'
    _MOBILE = '[data-qa="mobile_number"]'
    _CREATE_ACCOUNT_BUTTON = '[data-qa="create-account"]'
    _CONTINUE_BUTTON = '[data-qa="continue-button"]'

    def fill_account_details(
        self,
        password: str,
        firstname: str,
        lastname: str,
        address: str,
        country: str,
        state: str,
        city: str,
        zipcode: str,
        mobile: str,
        title: str = "Mr",
        day: str = "10",
        month: str = "May",
        year: str = "1990",
    ) -> "RegistrationPage":
        if title.lower() == "mr":
            self.click(self._MR_TITLE)
        else:
            self.click(self._MRS_TITLE)

        self.fill(self._PASSWORD, password)
        self.select_option(self._DAY, day)
        self.select_option(self._MONTH, month)
        self.select_option(self._YEAR, year)
        self.fill(self._FIRSTNAME, firstname)
        self.fill(self._LASTNAME, lastname)
        self.fill(self._ADDRESS, address)
        self.select_option(self._COUNTRY, country)
        self.fill(self._STATE, state)
        self.fill(self._CITY, city)
        self.fill(self._ZIPCODE, zipcode)
        self.fill(self._MOBILE, mobile)
        return self

    def submit(self) -> "RegistrationPage":
        self.click(self._CREATE_ACCOUNT_BUTTON)
        self.assert_text_visible("Account Created!")
        self.click(self._CONTINUE_BUTTON)
        return self
