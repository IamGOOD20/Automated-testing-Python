from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    url = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        print('current link: ', self.browser.current_url)
        assert '/login' in self.browser.current_url, '"login not found in current url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'login form not found'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'registration form not found'

