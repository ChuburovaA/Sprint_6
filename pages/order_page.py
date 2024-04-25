import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
import random

class OrderPage(BasePage):

    @allure.step('Оформление заказа: заполнены все поля ввода')
    def set_form_to_order(self, rent, checkbox, comment):
        # Страница "Для кого самокат"
        self.add_text_to_element(OrderPageLocators.ORDER_PAGE_NAME, 'Ольга')
        self.add_text_to_element(OrderPageLocators.ORDER_PAGE_SURNAME, 'Воронова')
        self.add_text_to_element(OrderPageLocators.ORDER_PAGE_ADDRESS, 'Петропаловская улица, дом 10')
        self.select_element_from_list(OrderPageLocators.ORDER_PAGE_METRO_STATION_BUTTON,
                                      self.set_number_to_locator(OrderPageLocators.ORDER_PAGE_METRO_STATION,
                                                                 random.randint(0, 224)))
        self.add_text_to_element(OrderPageLocators.ORDER_PAGE_PHONE_NUMBER, '+71234567890')
        self.click_to_element(OrderPageLocators.ORDER_PAGE_BUTTON_NEXT)

        # Страница "Про аренду"
        self.add_text_to_element(OrderPageLocators.ORDER_PAGE_DATE, random.randint(1, 99999))
        self.click_to_element(OrderPageLocators.ORDER_PAGE_ACCEPT_DATE)
        self.select_element_from_list(OrderPageLocators.ORDER_PAGE_RENT_TIME, rent)
        self.click_to_element(checkbox)
        self.add_text_to_element(OrderPageLocators.ORDER_PAGE_COMMENT_FOR_COURIER, comment)
        self.find_element_with_wait(OrderPageLocators.ORDER_PAGE_ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.ORDER_PAGE_ORDER_BUTTON)

        # Подтверждение заказа
        self.click_to_element(OrderPageLocators.ORDER_PAGE_BUTTON_YES)