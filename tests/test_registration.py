from tests.base_test import BaseTest
from pages.search_page import SearchPage

class TestGoogleSearch(BaseTest):
    def test_search_squirt(self):
        page = SearchPage(self.driver)
        page.googleSearch("Rafaella Barrocas Senior QA Engineer Linkedin")