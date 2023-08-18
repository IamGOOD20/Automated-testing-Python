from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-cart')
    PRODUCT_TITLE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    PRODUCT_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]//p[@class="price_color"]')
    BASKET_ADDED_MASSAGE = (By.XPATH, '//div[@id="messages"]/div/div/strong')
    BASKET_TOTAL_PRICE = (By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-info  fade in"]/div/p/strong')
