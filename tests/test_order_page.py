import allure
import pytest
from locators.order_page_locators import OrderPageLocators

from conftest import driver, main_page, order_page

@allure.feature('Заказ самоката на сайте "Яндекс Самокат"')
class TestOrderPage:
    @allure.story('Заполнение форм "Для кого самокат" и "Про аренду"')
    @pytest.mark.parametrize("button, rent, checkbox, comment",
                             [(OrderPageLocators.ORDER_BUTTON_UP,
                               OrderPageLocators.ORDER_PAGE_RENT_TO_ONE_DAY,
                               OrderPageLocators.ORDER_PAGE_BLACK_CHECKBOX,
                               'Опаздаю!'),
                              (OrderPageLocators.ORDER_BUTTON_DOWN,
                               OrderPageLocators.ORDER_PAGE_RENT_TO_TWO_DAYS,
                               OrderPageLocators.ORDER_PAGE_GREY_CHECKBOX,
                               'Sorry, ill be 10min late')
                              ])