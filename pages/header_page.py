import allure

from locators.header_page_locators import HeaderPageLocators
from pages.base_page import BasePage

class HeaderPage(BasePage):

    @allure.step('Кликнуть на лого Яндекса')
    def click_yandex_logo(self):
        self.click_to_element(HeaderPageLocators.HEADER_PAGE_LOGO_YANDEX)

    @allure.step('Дождаться на другой странице лого Дзена')
    def switch_to_dzen(self):
        self.wait_element(HeaderPageLocators.HEADER_PAGE_BUTTON_FIND)