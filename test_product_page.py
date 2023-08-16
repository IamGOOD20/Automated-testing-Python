from pages.product_page import ProductPage
from time import sleep

def test_quest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product = ProductPage(browser, link)
    product.open()
    product.add_to_basket()
    product.solve_quiz_and_get_code()
    sleep(30)
