from turtle import home
from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage

class TestSignIn(BaseTest):

    def setUp(self):
        self.home = HomePage(self.driver)
        self.si = SignInPage(self.driver)

    def test_sign_in(self):
        self.home.navigate_to_sign_in_page()
        self.si.enter_email(email='ADD_YOUR_EMAIL_HERE')
        self.si.enter_password(password='ADD_YOUR_PASSWORD_HERE')
        self.home.validate_user_is_signed_in(isDisplayed=True)

    def test_sign_in_with_invalid_credentials(self):
        self.home.navigate_to_sign_in_page()
        self.si.enter_email(email='ADD_INVALID_EMAIL_HERE')
        self.si.enter_password(password='ADD_INVALID_PASSWORD_HERE')
        self.home.validate_user_is_signed_in(isDisplayed=False)