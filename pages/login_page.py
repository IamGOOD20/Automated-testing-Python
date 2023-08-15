from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self, browser):
        assert 'login' in browser.current_url, '"login not found in current url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL,
                                       LoginPageLocators.LOGIN_PASSWORD), 'login form not found'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL, LoginPageLocators.REGISTER_PASSWORD,
                                LoginPageLocators.REGISTER_CONFIRM_PASSWORD), 'registration form not found'
