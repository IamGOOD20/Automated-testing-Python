from pages.base_page import BasePage
from.locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        self.click_add_to_basket_button()

    def check_basket_on_added_product_and_total_basket(self):
        self.should_be_message_added_product_title_in_basket()
        self.should_be_correct_basket_total_after_added_product()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), 'basket button not found'

    def click_add_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_product_title_on_page(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE), 'product title in store not found'
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_product_price_on_page(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), 'product price in store not found'
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_product_title_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_ADDED_MASSAGE), 'product title not found in basket'
        return self.browser.find_element(*ProductPageLocators.BASKET_ADDED_MASSAGE).text

    def get_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_PRICE), 'basket total not found'
        return self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text

    def should_be_message_added_product_title_in_basket(self):
        assert self.get_product_title_on_page() == self.get_product_title_in_basket(), "product wasn't added to basket"

    def should_be_correct_basket_total_after_added_product(self):
        assert self.get_product_price_on_page() == self.get_basket_total(), 'The price of product != total of basket'



