import pytest
import selene
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='function', autouse=True)
def browser_managment():
    browser.config.base_url = 'https://todomvc.com/examples/emberjs/'
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options
    browser.config.type_by_js = True

    yield

    browser.quit()