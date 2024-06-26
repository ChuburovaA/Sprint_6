import pytest
from selenium import webdriver

from constans import Urls
from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.order_page import OrderPage

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()

    yield driver

    driver.quit()

@pytest.fixture(scope='function')
def main_page(driver):
    driver.get(Urls.URL)
    mp = MainPage(driver)
    return mp

@pytest.fixture(scope='function')
def header_page(driver):
    hp = HeaderPage(driver)
    return hp

@pytest.fixture(scope='function')
def order_page(driver):
    op = OrderPage(driver)
    return op

