from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/'


def go_to_login_page(browser):
    browser.find_element(By.CSS_SELECTOR, "#login_link").click()

def test_quest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)


