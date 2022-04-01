from utils.locators import RegisterPageLocators

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        self.locator = RegisterPageLocators
        super(RegistrationPage, self).__init__(driver)

    def register_new_user(self, name, email, password, password_check):
        self.find_element(*self.locator.NAME_INPUT).send_keys(name)
        self.find_element(*self.locator.EMAIL_INPUT).send_keys(email)
        self.find_element(*self.locator.PASSWORD_INPUT).send_keys(password)
        self.find_element(*self.locator.PASSWORD_CHECK_INPUT).send_keys(password_check)
        self.find_element(*self.locator.CONTINUE_BUTTON).click()

    def validate_invalid_name(self):
        assert self.find_element(*self.locator.INVALID_NAME_MESSAGE).isDisplayed()

    def validate_invalid_email(self):
        assert self.find_element(*self.locator.INVALID_EMAIL_MESSAGE).isDisplayed()

    def validate_password_mismatch(self):
        assert self.find_element(*self.locator.PASSWORD_MISMATCH_MESSAGE).isDisplayed()
