from pages.base_page import BasePage
from.locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        self.get_product_price()
        self.get_product_title()
        self.should_be_basket_button()
        self.click_basket_button()

    def check_basket_on_added_product_and_total_basket(self):
        self.should_be_message_added_product_title_in_basket()
        self.should_be_correct_basket_total_after_added_product()


    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), 'basket button not found'

    def click_basket_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_product_title(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE), 'product title not found'
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        return product_title

    def get_product_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE), 'product price not found'
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def should_be_message_added_product_title_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text \
               in self.get_product_title(), "The product wasn't added to basket" # self.browser.find_element(*ProductPageLocators.BASKET_ADDED_MASSAGE)

    def should_be_correct_basket_total_after_added_product(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text \
               == self.get_product_price(), 'The price of product != total of basket'# self.browser.find_element
