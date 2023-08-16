from pages.base_page import BasePage
from.locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        self.should_be_basket_button()
        self.click_basket_button()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), 'basket button not found'

    def click_basket_button(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()
    # def should_add_