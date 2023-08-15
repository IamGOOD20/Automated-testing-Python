from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_EMAIL = (By.NAME, 'login-username') # [name= ]
    LOGIN_PASSWORD = (By.NAME, 'login-password')
    REGISTER_EMAIL = (By.NAME, 'registration-email')
    REGISTER_PASSWORD = (By.NAME, 'registration-password1')
    REGISTER_CONFIRM_PASSWORD = (By.NAME, 'registration-password2')