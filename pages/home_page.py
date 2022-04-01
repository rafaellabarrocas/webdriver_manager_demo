from curses import KEY_ENTER
from pages.base_page import BasePage
from utils.locators import HomePageLocators
from selenium.webdriver.common.keys import Keys

class HomePage(BasePage):
    def __init__(self, driver):
        self.locator = HomePageLocators
        super(SearchPage, self).__init__(driver)

    def navigate_to_sign_in_page(self):
        self.find_element(*self.locator.LOGIN_LINK).click()

    def navigate_to_register_page(self):
        self.find_element(*self.locator.REGISTER_LINK).click()