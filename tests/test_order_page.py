import allure
import pytest
from locators.order_page_locators import OrderPageLocators

from conftest import driver, main_page, order_page

@allure.feature('Заказ самоката на сайте "Яндекс Самокат"')
class TestOrderPage: