import allure
import pytest
from locators.order_page_locators import OrderPageLocators

from conftest import driver, main_page, order_page

@allure.feature('Заказ самоката на сайте "Яндекс Самокат"')
class TestOrderPage:
    @allure.title('Заполнение форм "Для кого самокат" и "Про аренду"')
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
    def test_to_order(self, main_page, order_page, button, rent, checkbox, comment):
        main_page.click_button_cookie()
        order_page.scroll_down(button)
        order_page.click_to_element(button)
        order_page.set_form_to_order(rent, checkbox, comment)
        assert main_page.check_order_button()