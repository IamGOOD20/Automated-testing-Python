from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/'


def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link").click()
