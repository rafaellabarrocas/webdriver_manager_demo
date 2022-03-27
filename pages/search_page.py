from curses import KEY_ENTER
from pages.base_page import BasePage
from utils.locators import SearchPageLocators
import time
from selenium.webdriver.common.keys import Keys

class SearchPage(BasePage):
    def __init__(self, driver):
        self.locator = SearchPageLocators
        super(SearchPage, self).__init__(driver)

    def googleSearch(self, text):
        self.find_element(*self.locator.SEARCH_INPUT).send_keys(text)
        time.sleep(3)
        self.find_element(*self.locator.SEARCH_INPUT).send_keys(Keys.RETURN)
        time.sleep(3)