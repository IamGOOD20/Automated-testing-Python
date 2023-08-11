import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope=None)
def browser(request):
    user_language = request.config.getoption('language')
    browser = webdriver.Chrome()
    if user_language:
        print('\nStart browser')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    yield browser
    print('\nBrowser quit')
    browser.quit()


