import pytest
from pages.product_page import ProductPage
from time import sleep

# for i in range(0, 10):
#     @pytest.mark.parametrize('link', f'[http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}]')
#     def test_quest_can_add_product_to_basket(browser, link):
#         # link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#         product = ProductPage(browser, link)
#         product.open()
#         product.add_to_basket()
#         product.solve_quiz_and_get_code()


# @pytest.mark.parametrize('link',["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_quest_can_add_product_to_basket(browser): # , link
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product = ProductPage(browser, link)
    product.open()
    product.add_to_basket()
    product.solve_quiz_and_get_code()
    product.check_basket_on_added_product_and_total_basket()

