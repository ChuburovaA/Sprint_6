import allure

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step('Открыть страницу')
    def get_url(self, url):
        self.driver.get(url)

    @allure.step('Кликнуть на кнопку принятия кук')
    def click_button_cookie(self):
        return self.click_to_element(MainPageLocators.MAIN_PAGE_COOKIE_BUTTON)