from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name

class HomePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href*='signin?'")
    REGISTER_LINK = (By.CSS_SELECTOR, "a[href*='register?'")

class LoginPageLocators(object):
    EMAIL_INPUT = (By.ID, 'ap_email')
    CONTINUE_BUTTON = (By.ID, 'continue')
    PASSWORD_INPUT = (By.ID, 'ap_password')
    SIGN_IN_BUTTON = (By.ID, 'signInSubmit')

class RegisterPageLocators(object):
    NAME_INPUT = (By.ID, 'ap_customer_name')
    EMAIL_INPUT = (By.ID, 'ap_email')
    PASSWORD_INPUT = (By.ID, 'ap_password')
    PASSWORD_CHECK_INPUT = (By.ID, 'ap_password_check')
    CONTINUE_BUTTON = (By.ID, 'continue')