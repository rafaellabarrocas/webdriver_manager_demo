from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name

class SearchPageLocators(object):
    SEARCH_INPUT = (By.NAME, 'q')
    SEARCH_BUTTON = (By.NAME, 'btnK')