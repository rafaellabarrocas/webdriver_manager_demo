from tests.base_test import BaseTest
from pages.registration_page import RegistrationPage
from pages.home_page import HomePage
from faker import Faker

class TestRegistration(BaseTest):

    def setUp(self):
        self.home = HomePage(self.driver)
        self.r = RegistrationPage(self.driver)

        self.fake = Faker()

    def test_registration(self):
        self.home.navigate_to_register_page()
        self.r.register_new_user(name=self.fake.name(), email=self.fake.email(), 
                                password='123456',
                                password_check='123456')
        self.home.validate_user_is_signed_in()

    def test_registration_invalid_name(self):
        self.home.navigate_to_register_page()
        self.r.register_new_user(name='', email=self.fake.email(), 
                                password='123456',
                                password_check='123456')
        self.r.validate_invalid_name()
    
    def test_registration_invalid_email(self):
        self.home.navigate_to_register_page()
        self.r.register_new_user(name=self.fake.name(), email='test', 
                                password='123456',
                                password_check='123456')
        self.r.validate_invalid_email()

    def test_registration_password_mismatch(self):
        self.home.navigate_to_register_page()
        self.r.register_new_user(name=self.fake.name(), email=self.fake.email(), 
                                password='123456',
                                password_check='123856')
        self.r.validate_password_mismatch()
        