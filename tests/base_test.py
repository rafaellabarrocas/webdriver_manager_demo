import unittest

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service

from selenium import webdriver
import time

class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        # options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox')  # # Bypass OS security model
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--start-fullscreen")
        options.add_argument('--disable-gpu')

        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get("http://www.amazon.com")
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()