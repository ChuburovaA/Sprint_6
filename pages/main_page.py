import allure

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step('Открыть страницу')
    def get_url(self, url):
        self.driver.get(url)