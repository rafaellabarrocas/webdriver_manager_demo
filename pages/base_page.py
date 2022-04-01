class BasePage(object):
    def __init__(self, driver, base_url='http://www.amazon.com/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)