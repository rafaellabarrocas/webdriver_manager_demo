from curses import KEY_ENTER
from pages.base_page import BasePage
from utils.locators import LoginPageLocators
from selenium.webdriver.common.keys import Keys

class SignInPage(BasePage):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super(SearchPage, self).__init__(driver)

    def enter_email(self, email):
        self.find_element(*self.locator.EMAIL_INPUT).sendKeys(email)
        self.find_element(*self.locator.CONTINUE_BUTTON).click()

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD_INPUT).sendKeys(password)
        self.find_element(*self.locator.SIGN_IN_BUTTON).click()