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

    @allure.step('Кликнуть на лого Самоката')
    def click_logo_scooter(self):
        self.click_to_element(HeaderPageLocators.HEADER_PAGE_LOGO_SCOOTER)

    @allure.step('Получить текст на главной')
    def get_text(self):
        text = self.get_text_from_element(HeaderPageLocators.HEADER_PAGE_TEXT)
        return text